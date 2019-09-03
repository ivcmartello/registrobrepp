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
        assert xml == checkasncommandxmlexpected

    def test_check_asn_response(self, asnxmlschema, responsecheckasncommandxmlexpected):
        response = EppResponse.from_xml(responsecheckasncommandxmlexpected,
                                        extra_nsmap={'asn': 'urn:ietf:params:xml:ns:asn-1.0'})
        xml = response.to_xml(force_prefix=True).decode()
        cd = response['epp']['response']['resData']['asn:chkData']['cd']

        assert cd.number['@avail'] == '0'
        assert cd.number['_text'] == '64500'
        assert cd.reason == 'In use'
        assert response['epp']['response']['trID']['clTRID'] == 'ABC-12345'
        assert response['epp']['response']['trID']['svTRID'] == '54322-XYZ'
        assert asnxmlschema.validate(etree.fromstring(xml))
