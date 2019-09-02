from eppy.doc import EppResponse
from lxml import etree

from registrobrepp.asn.brcheckasncommand import BrEppCheckAsnCommand


class TestBrCheckAsnCommand:

    def test_check_asn_command(self, asnxmlschema, checkasncommandxmlexpected):
        numbers = [12345, 11111]
        command = BrEppCheckAsnCommand(numbers)
        command.add_clTRID('ABC-12345')
        xml = command.to_xml(force_prefix=True).decode()

        assert asnxmlschema.validate(etree.fromstring(xml))
        assert checkasncommandxmlexpected == xml

    def test_check_asn_response(self, asnxmlschema, responsecheckasncommandxmlexpected):
        response = EppResponse.from_xml(responsecheckasncommandxmlexpected,
                                        extra_nsmap={'asn': 'urn:ietf:params:xml:ns:asn-1.0'})
        xml = response.to_xml(force_prefix=True).decode()
        cd = response['epp']['response']['resData']['asn:chkData']['cd']

        assert '0' == cd.number['@avail']
        assert '64500' == cd.number['_text']
        assert 'In use' == cd.reason
        assert 'ABC-12345' == response['epp']['response']['trID']['clTRID']
        assert '54322-XYZ' == response['epp']['response']['trID']['svTRID']
        assert asnxmlschema.validate(etree.fromstring(xml))
