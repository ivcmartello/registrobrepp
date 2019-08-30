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
        xml = contactcommand.to_xml(force_prefix=False).decode()

        assert contactxmlschema.validate(etree.fromstring(xml))
        assert checkcontactcommandxmlexpected == xml

    def test_check_domain_command_with_brorg_extension(self, contactcommand, brorgxmlschema, checkcontactcommandwithbrorgxmlexpected):
        cds = [Cd('e123456', '043.828.151/0001-45'), Cd('e654321', '005.506.560/0001-36')]
        brorg = EppCheckBrOrg(cds)
        brorgxml = brorg.to_xml(force_prefix=False).decode()
        contactcommand.add_command_extension(brorg)
        commandxml = contactcommand.to_xml(force_prefix=False).decode()

        assert brorgxmlschema.validate(etree.fromstring(brorgxml))
        assert checkcontactcommandwithbrorgxmlexpected == commandxml

    def test_check_contact_response(self, contactxmlschema, responsecheckcontactcommandxmlexpected):
        response = EppResponse.from_xml(responsecheckcontactcommandxmlexpected)
        xml = response.to_xml(force_prefix=False).decode()
        cds = response['epp']['response']['resData']['contact:chkData']['cd']

        assert '1' == cds[0]['id']['@avail']
        assert 'sh8013' == cds[0]['id']['_text']
        assert '0' == cds[1]['id']['@avail']
        assert 'sah8013' == cds[1]['id']['_text']
        assert 'In use' == cds[1]['reason']
        assert '1' == cds[2]['id']['@avail']
        assert '8013sah' == cds[2]['id']['_text']
        assert 'ABC-12345' == response['epp']['response']['trID']['clTRID']
        assert '54322-XYZ' == response['epp']['response']['trID']['svTRID']
        assert contactxmlschema.validate(etree.fromstring(xml))
        assert responsecheckcontactcommandxmlexpected == xml

    def test_check_contact_with_brorg_response(self, responsecheckcontactcommandwithbrorgxmlexpected):
        response = EppResponse.from_xml(responsecheckcontactcommandwithbrorgxmlexpected,
                                        extra_nsmap={'brorg': 'urn:ietf:params:xml:ns:brorg-1.0'})
        extension = response.get_response_extension('brorg:chkData')
        tickets = extension['ticketInfo']

        assert '006.994.175/0001-48' == tickets[0].organization
        assert '2822407' == tickets[0].ticketNumber
        assert 'doremisolfalasi.com.br' == tickets[0].domainName
        assert '067.774.281/0001-00' == tickets[1].organization
        assert '2822403' == tickets[1].ticketNumber
        assert 'edpgviva.com.br' == tickets[1].domainName
