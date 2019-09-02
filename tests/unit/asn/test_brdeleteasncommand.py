from eppy.doc import EppResponse
from lxml import etree

from registrobrepp.asn.brdeleteasncommand import BrEppDeleteAsnCommand


class TestBrDeleteAsnCommand:

    def test_delete_asn_command(self, asnxmlschema, deleteasncommandxmlexpected):
        number = 64500
        command = BrEppDeleteAsnCommand(number)
        command.add_clTRID('ABC-12345')
        xml = command.to_xml(force_prefix=True).decode()

        assert asnxmlschema.validate(etree.fromstring(xml))
        assert deleteasncommandxmlexpected == xml

    def test_delete_asn_response(self, asnxmlschema, responsedeleteasncommandxmlexpected):
        response = EppResponse.from_xml(responsedeleteasncommandxmlexpected,
                                        extra_nsmap={'asn': 'urn:ietf:params:xml:ns:asn-1.0'})
        xml = response.to_xml(force_prefix=True).decode()

        assert 'ABC-12345' == response['epp']['response']['trID']['clTRID']
        assert '54321-XYZ' == response['epp']['response']['trID']['svTRID']
        assert asnxmlschema.validate(etree.fromstring(xml))
