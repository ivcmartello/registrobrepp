import pytest
from eppy.doc import EppResponse
from lxml import etree

from registrobrepp.contact.addr import Addr
from registrobrepp.authinfo import AuthInfo
from registrobrepp.contact.brcreatecontactcommand import BrEppCreateContactCommand
from registrobrepp.contact.disclose import Disclose
from registrobrepp.contact.eppcreatelacniccontact import EppCreateLacnicContact
from registrobrepp.contact.phone import Phone
from registrobrepp.contact.postalinfo import PostalInfo


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
        xml = createcontactcommand.to_xml(force_prefix=False).decode()

        assert contactxmlschema.validate(etree.fromstring(xml))
        assert createcontactcommandxmlexpected == xml

    def test_create_contact_with_lacnic_command(self, createcontactcommand, createcontactcommandwithlacnicxmlexpected):
        lacnic = EppCreateLacnicContact('abc123')
        createcontactcommand.add_command_extension(lacnic)
        xml = createcontactcommand.to_xml(force_prefix=False).decode()

        assert createcontactcommandwithlacnicxmlexpected == xml

    def test_create_contact_response(self, contactxmlschema, responsecreatecontactcommandxmlexpected):
        response = EppResponse.from_xml(responsecreatecontactcommandxmlexpected)
        xml = response.to_xml(force_prefix=False).decode()
        data = response['epp']['response']['resData']['contact:creData']

        assert 'sh8013' == data['id']
        assert '1999-04-03T22:00:00.0Z' == data['crDate']
        assert 'ABC-12345' == response['epp']['response']['trID']['clTRID']
        assert '54321-XYZ' == response['epp']['response']['trID']['svTRID']
        assert contactxmlschema.validate(etree.fromstring(xml))
        assert responsecreatecontactcommandxmlexpected == xml
