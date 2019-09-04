import datetime

import pytest
from eppy.doc import EppResponse
from lxml import etree

from registrobrepp.common.statustype import StatusContactType
from registrobrepp.contact.addbrorg import AddBrOrg
from registrobrepp.contact.addlacniccontact import AddLacnicContact
from registrobrepp.contact.addlacnicorg import AddLacnicOrg
from registrobrepp.contact.addr import Addr
from registrobrepp.common.authinfo import AuthInfo
from registrobrepp.contact.brupdatecontactcommand import BrEppUpdateContactCommand
from registrobrepp.contact.chgbrorg import ChgBrOrg
from registrobrepp.contact.chgcontact import ChgContact
from registrobrepp.contact.chglacniccontact import ChgLacnicContact
from registrobrepp.contact.chglacnicorg import ChgLacnicOrg
from registrobrepp.contact.contactbrorg import ContactBrOrg
from registrobrepp.contact.contactbrorgtype import ContactBrOrgType
from registrobrepp.contact.eppstatus import EppStatus
from registrobrepp.contact.eppupdatebrorg import EppUpdateBrOrg
from registrobrepp.contact.eppupdatelacniccontact import EppUpdateLacnicContact
from registrobrepp.contact.eppupdatelacnicorg import EppUpdateLacnicOrg
from registrobrepp.contact.orgtype import OrgType
from registrobrepp.contact.property import Property
from registrobrepp.contact.rembrorg import RemBrOrg
from registrobrepp.contact.remlacniccontact import RemLacnicContact
from registrobrepp.common.status import StatusContact
from registrobrepp.contact.disclose import Disclose
from registrobrepp.contact.phone import Phone
from registrobrepp.contact.postalinfo import PostalInfo
from registrobrepp.contact.remlacnicorg import RemLacnicOrg
from registrobrepp.contact.renewaltype import RenewalType
from registrobrepp.contact.resourcesclass import ResourcesClass


class TestBrUpdateContactCommand:

    @pytest.fixture
    def updatecontactcommand(self):
        authinfo = AuthInfo('123')
        addr = Addr('123 Example Dr.', 'Suite 100', 'Dulles', 'US', street3='xyz', sp='VA', pc='20166-6503')
        voice = Phone('1234', '+1.7035555555')
        postalinfo = PostalInfo.build('Joe Doe', addr, 'Example Inc.')
        postalinfo2 = PostalInfo.build('Anna Doe', addr, 'Example Inc.', international=True)
        disclose = Disclose(flag=True, name_int=True, org_int=True, addr_int=True, voice=True, fax=True, email=True)
        statusadd = [StatusContact(StatusContactType.CLIENTDELETEPROHIBITED)]
        statusrem = [StatusContact(StatusContactType.CLIENTDELETEPROHIBITED)]
        chg = ChgContact(postalinfo, 'jdoe@example.com', authinfo, postalinfo2=postalinfo2, voice=voice,
                         disclose=disclose)
        command = BrEppUpdateContactCommand('ab-12345', statusadd, status_rem=statusrem, chg=chg)
        command.add_clTRID('ABC-12345')
        return command

    def test_update_contact_command(self, updatecontactcommand, contactxmlschema, updatecontactcommandxmlexpected):
        xml = updatecontactcommand.to_xml(force_prefix=True).decode()

        assert contactxmlschema.validate(etree.fromstring(xml))
        assert xml == updatecontactcommandxmlexpected

    def test_update_contact_with_lacnic_command(self, updatecontactcommand, updatecontactcommandwithlacnicxmlexpected):
        add = [Property('bulkwhois')]
        add = AddLacnicContact(add)
        rem = [Property('inactive')]
        rem = RemLacnicContact(rem)
        chg = ChgLacnicContact('abc123')
        lacnic = EppUpdateLacnicContact(add, rem, chg)
        updatecontactcommand.add_command_extension(lacnic)
        xml = updatecontactcommand.to_xml(force_prefix=True).decode()

        assert xml == updatecontactcommandwithlacnicxmlexpected

    def test_update_contact_command_with_brorg_and_lacnicorg_extension(self, updatecontactcommand, brorgxmlschema,
                                                                       lacnicorgxmlschema,
                                                                       updatecontactcommandwithbrorgandlacnicorgxmlexpected):
        add = AddBrOrg(ContactBrOrg(ContactBrOrgType.ADMIN, 'hkk'))
        rem = RemBrOrg(ContactBrOrg(ContactBrOrgType.ADMIN, 'fan'))
        chg = ChgBrOrg('Responsible Name', datetime.datetime(2009, 2, 1, 12, 00, 00), suspended=True)
        brorg = EppUpdateBrOrg('005.506.560/0001-36', add, rem, chg)
        brorgxml = brorg.to_xml(force_prefix=True).decode()

        add = AddLacnicOrg(['192.168.0.1', '192.0.2.0/24'], RenewalType.LARGE)
        rem = RemLacnicOrg(['203.0.113.0/24'], RenewalType.SMALL)
        chg = ChgLacnicOrg(OrgType.NORMAL, EppStatus.ACTIVE, 'abc123', ResourcesClass.NON_LEGACY_ONLY)
        lacnicorg = EppUpdateLacnicOrg('abc123', add, rem, chg)
        lacnicorgxml = lacnicorg.to_xml(force_prefix=True).decode()

        updatecontactcommand.add_command_extension(brorg)
        updatecontactcommand.add_command_extension(lacnicorg)
        xml = updatecontactcommand.to_xml(force_prefix=True).decode()

        assert brorgxmlschema.validate(etree.fromstring(brorgxml))
        assert lacnicorgxmlschema.validate(etree.fromstring(lacnicorgxml))
        assert xml == updatecontactcommandwithbrorgandlacnicorgxmlexpected

    def test_update_contact_response(self, contactxmlschema, responseupdatecontactcommandxmlexpected):
        response = EppResponse.from_xml(responseupdatecontactcommandxmlexpected)
        xml = response.to_xml(force_prefix=True).decode()

        assert response['epp']['response']['trID']['clTRID'] == 'ABC-12345'
        assert response['epp']['response']['trID']['svTRID'] == '54321-XYZ'
        assert contactxmlschema.validate(etree.fromstring(xml))
        assert xml == responseupdatecontactcommandxmlexpected
