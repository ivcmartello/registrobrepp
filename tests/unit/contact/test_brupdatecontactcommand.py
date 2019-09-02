import pytest
from eppy.doc import EppResponse
from lxml import etree

from registrobrepp.contact.addlacniccontact import AddLacnicContact
from registrobrepp.contact.addr import Addr
from registrobrepp.common.authinfo import AuthInfo
from registrobrepp.contact.brupdatecontactcommand import BrEppUpdateContactCommand
from registrobrepp.contact.chgcontact import ChgContact
from registrobrepp.contact.chglacniccontact import ChgLacnicContact
from registrobrepp.contact.eppupdatelacniccontact import EppUpdateLacnicContact
from registrobrepp.contact.property import Property
from registrobrepp.contact.remlacniccontact import RemLacnicContact
from registrobrepp.common.status import Status
from registrobrepp.contact.disclose import Disclose
from registrobrepp.contact.phone import Phone
from registrobrepp.contact.postalinfo import PostalInfo


class TestBrUpdateContactCommand:

    @pytest.fixture
    def updatecontactcommand(self):
        authinfo = AuthInfo('123')
        addr = Addr('123 Example Dr.', 'Suite 100', 'Dulles', 'US', street3='xyz', sp='VA', pc='20166-6503')
        voice = Phone('1234', '+1.7035555555')
        postalinfo = PostalInfo.build('Joe Doe', addr, 'Example Inc.')
        postalinfo2 = PostalInfo.build('Anna Doe', addr, 'Example Inc.', international=True)
        disclose = Disclose(flag=True, name_int=True, org_int=True, addr_int=True, voice=True, fax=True, email=True)
        statusadd = [Status(s='clientDeleteProhibited')]
        statusrem = [Status(s='clientDeleteProhibited')]
        chg = ChgContact(postalinfo, 'jdoe@example.com', authinfo, postalinfo2=postalinfo2, voice=voice,
                         disclose=disclose)
        command = BrEppUpdateContactCommand('ab-12345', statusadd, status_rem=statusrem, chg=chg)
        command.add_clTRID('ABC-12345')
        return command

    def test_update_contact_command(self, updatecontactcommand, contactxmlschema, updatecontactcommandxmlexpected):
        xml = updatecontactcommand.to_xml(force_prefix=True).decode()

        assert contactxmlschema.validate(etree.fromstring(xml))
        assert updatecontactcommandxmlexpected == xml

    def test_update_contact_with_lacnic_command(self, updatecontactcommand, updatecontactcommandwithlacnicxmlexpected):
        add = [Property('bulkwhois')]
        add = AddLacnicContact(add)
        rem = [Property('inactive')]
        rem = RemLacnicContact(rem)
        chg = ChgLacnicContact('abc123')
        lacnic = EppUpdateLacnicContact(add, rem, chg)
        updatecontactcommand.add_command_extension(lacnic)
        xml = updatecontactcommand.to_xml(force_prefix=True).decode()

        assert updatecontactcommandwithlacnicxmlexpected == xml

    def test_update_contact_response(self, contactxmlschema, responseupdatecontactcommandxmlexpected):
        response = EppResponse.from_xml(responseupdatecontactcommandxmlexpected)
        xml = response.to_xml(force_prefix=True).decode()

        assert 'ABC-12345' == response['epp']['response']['trID']['clTRID']
        assert '54321-XYZ' == response['epp']['response']['trID']['svTRID']
        assert contactxmlschema.validate(etree.fromstring(xml))
        assert responseupdatecontactcommandxmlexpected == xml
