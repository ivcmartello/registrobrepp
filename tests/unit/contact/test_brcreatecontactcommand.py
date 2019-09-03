import pytest
from eppy.doc import EppResponse
from lxml import etree

from registrobrepp.contact.addr import Addr
from registrobrepp.common.authinfo import AuthInfo
from registrobrepp.contact.brcreatecontactcommand import BrEppCreateContactCommand
from registrobrepp.contact.contactbrorg import ContactBrOrg
from registrobrepp.contact.disclose import Disclose
from registrobrepp.contact.eppcreatebrorg import EppCreateBrOrg
from registrobrepp.contact.eppcreatelacniccontact import EppCreateLacnicContact
from registrobrepp.contact.eppcreatelacnicorg import EppCreateLacnicOrg
from registrobrepp.contact.orgtype import OrgType
from registrobrepp.contact.phone import Phone
from registrobrepp.contact.postalinfo import PostalInfo
from registrobrepp.contact.renewaltype import RenewalType
from registrobrepp.contact.resourcesclass import ResourcesClass


class TestBrCreateContactCommand:

    @pytest.fixture
    def createcontactcommand(self):
        addr = Addr('123 Example Dr.', 'Suite 100', 'Dulles', 'US', street3='xyz', sp='VA', pc='20166-6503')
        voice = Phone('1234', '+1.7035555555')
        postalinfo = PostalInfo.build('Joe Doe', addr, 'Example Inc.')
        postalinfo2 = PostalInfo.build('Anna Doe', addr, 'Example Inc.', international=True)
        authinfo = AuthInfo('123')
        disclose = Disclose(flag=True, name_loc=True, org_loc=True, addr_loc=True, voice=True, fax=True, email=True)
        command = BrEppCreateContactCommand('ab-12345', postalinfo, 'jdoe@example.com', authinfo,
                                            postalinfo2=postalinfo2, voice=voice, disclose=disclose)
        command.add_clTRID('ABC-12345')
        return command

    def test_create_contact_command(self, createcontactcommand, contactxmlschema, createcontactcommandxmlexpected):
        xml = createcontactcommand.to_xml(force_prefix=True).decode()

        assert contactxmlschema.validate(etree.fromstring(xml))
        assert xml == createcontactcommandxmlexpected

    def test_create_contact_command_with_lacnic_extension(self, createcontactcommand, createcontactcommandwithlacnicxmlexpected):
        lacnic = EppCreateLacnicContact('abc123')
        createcontactcommand.add_command_extension(lacnic)
        xml = createcontactcommand.to_xml(force_prefix=True).decode()

        assert xml == createcontactcommandwithlacnicxmlexpected

    def test_create_contact_command_with_brorg_lacnicorg_extension(self, brorgxmlschema, lacnicorgxmlschema, createcontactcommand, createcontactcommandwithbrorglacnicorgxmlexpected):
        organization = '005.506.560/0001-36'
        contacts = [ContactBrOrg.build('fan', admin=True), ContactBrOrg.build('fun'),
                    ContactBrOrg.build('fuc', member=True)]
        responsible = 'John Doe'
        brorg = EppCreateBrOrg(organization, contacts, responsible)
        createcontactcommand.add_command_extension(brorg)
        brorgxml = brorg.to_xml(force_prefix=True).decode()

        eppips = ['192.168.0.1', '192.0.2.0/24', '203.0.113.0/24']
        renewtypes = [RenewalType.MEMBER, RenewalType.SMALL, RenewalType.FOUNDING_PARTNER]
        lacnicorg = EppCreateLacnicOrg(OrgType.NORMAL, 'abc123', eppips, renewtypes, ResourcesClass.ALL_RESOURCES)
        createcontactcommand.add_command_extension(lacnicorg)
        lacnicorgxml = lacnicorg.to_xml(force_prefix=True).decode()

        commandxml = createcontactcommand.to_xml(force_prefix=True).decode()

        assert brorgxmlschema.validate(etree.fromstring(brorgxml))
        assert lacnicorgxmlschema.validate(etree.fromstring(lacnicorgxml))
        assert commandxml == createcontactcommandwithbrorglacnicorgxmlexpected

    def test_create_contact_response(self, contactxmlschema, responsecreatecontactcommandxmlexpected):
        response = EppResponse.from_xml(responsecreatecontactcommandxmlexpected)
        xml = response.to_xml(force_prefix=True).decode()
        data = response['epp']['response']['resData']['contact:creData']

        assert data.id == 'sh8013'
        assert data.crDate == '1999-04-03T22:00:00.0Z'
        assert response['epp']['response']['trID']['clTRID'] == 'ABC-12345'
        assert response['epp']['response']['trID']['svTRID'] == '54321-XYZ'
        assert contactxmlschema.validate(etree.fromstring(xml))
        assert xml == responsecreatecontactcommandxmlexpected

    def test_create_contact_with_brorg_response(self, responsecreatecontactcommandwithbrorgxmlexpected):
        response = EppResponse.from_xml(responsecreatecontactcommandwithbrorgxmlexpected,
                                        extra_nsmap={'brorg': 'urn:ietf:params:xml:ns:brorg-1.0'})
        extension = response.get_response_extension('brorg:creData')

        assert extension.organization == '005.506.560/0001-36'
        assert response['epp']['response']['trID']['clTRID'] == 'ABC-12345'
        assert response['epp']['response']['trID']['svTRID'] == 'DEF-54321'
