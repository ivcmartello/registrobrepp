import pytest
from eppy.doc import EppResponse
from lxml import etree

from registrobrepp.contact.brcheckcontactcommand import BrEppCheckContactCommand
from registrobrepp.contact.cd import Cd
from registrobrepp.contact.eppcheckbrorg import EppCheckBrOrg


class TestBrCheckContactCommand:

    @pytest.fixture
    def contactcommand(self):
        ids = ['ab-12345', 'aa-11111']
        command = BrEppCheckContactCommand(ids)
        command.add_clTRID('ABC-12345')
        return command

    def test_check_contact_command(self, contactcommand, contactxmlschema, checkcontactcommandxmlexpected):
        xml = contactcommand.to_xml(force_prefix=True).decode()

        assert contactxmlschema.validate(etree.fromstring(xml))
        assert xml == checkcontactcommandxmlexpected

    def test_check_contact_command_with_brorg_extension(self, contactcommand, brorgxmlschema, checkcontactcommandwithbrorgxmlexpected):
        cds = [Cd('e123456', '043.828.151/0001-45'), Cd('e654321', '005.506.560/0001-36')]
        brorg = EppCheckBrOrg(cds)
        brorgxml = brorg.to_xml(force_prefix=True).decode()
        contactcommand.add_command_extension(brorg)
        commandxml = contactcommand.to_xml(force_prefix=True).decode()

        assert brorgxmlschema.validate(etree.fromstring(brorgxml))
        assert commandxml == checkcontactcommandwithbrorgxmlexpected

    def test_check_contact_response(self, contactxmlschema, responsecheckcontactcommandxmlexpected):
        response = EppResponse.from_xml(responsecheckcontactcommandxmlexpected)
        xml = response.to_xml(force_prefix=True).decode()
        cds = response['epp']['response']['resData']['contact:chkData']['cd']

        assert cds[0].id['@avail'] == '1'
        assert cds[0].id['_text'] == 'sh8013'
        assert cds[1].id['@avail'] == '0'
        assert cds[1].id['_text'] == 'sah8013'
        assert cds[1].reason == 'In use'
        assert cds[2].id['@avail'] == '1'
        assert cds[2].id['_text'] == '8013sah'
        assert response['epp']['response']['trID']['clTRID'] == 'ABC-12345'
        assert response['epp']['response']['trID']['svTRID'] == '54322-XYZ'
        assert contactxmlschema.validate(etree.fromstring(xml))
        assert xml == responsecheckcontactcommandxmlexpected

    def test_check_contact_with_brorg_response(self, responsecheckcontactcommandwithbrorgxmlexpected):
        response = EppResponse.from_xml(responsecheckcontactcommandwithbrorgxmlexpected,
                                        extra_nsmap={'brorg': 'urn:ietf:params:xml:ns:brorg-1.0'})
        extension = response.get_response_extension('brorg:chkData')
        tickets = extension['ticketInfo']

        assert tickets[0].organization == '006.994.175/0001-48'
        assert tickets[0].ticketNumber == '2822407'
        assert tickets[0].domainName == 'doremisolfalasi.com.br'
        assert tickets[1].organization == '067.774.281/0001-00'
        assert tickets[1].ticketNumber == '2822403'
        assert tickets[1].domainName == 'edpgviva.com.br'
