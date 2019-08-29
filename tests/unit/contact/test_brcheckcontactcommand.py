from eppy.doc import EppResponse
from lxml import etree

from registrobrepp.contact.brcheckcontactcommand import BrEppCheckContactCommand


class TestBrCheckContactCommand:

    def test_check_contact_command(self, contactxmlschema, checkcontactcommandxmlexpected):
        ids = ['ab-12345', 'aa-11111']
        command = BrEppCheckContactCommand(ids)
        command.add_clTRID('ABC-12345')
        xml = command.to_xml(force_prefix=False).decode()

        assert contactxmlschema.validate(etree.fromstring(xml))
        assert checkcontactcommandxmlexpected == xml

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
