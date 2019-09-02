from eppy.doc import EppResponse
from lxml import etree

from registrobrepp.asn.brdeletereserveasncommand import BrEppDeleteReserveAsnCommand


class TestBrDeleteReserveAsnCommand:

    def test_delete_reserve_asn_command(self, asnreservexmlschema, deletereserveasncommandxmlexpected):
        id = 64500
        command = BrEppDeleteReserveAsnCommand(id)
        command.add_clTRID('ABC-12345')
        xml = command.to_xml(force_prefix=True).decode()

        assert asnreservexmlschema.validate(etree.fromstring(xml))
        assert deletereserveasncommandxmlexpected == xml

    def test_delete_reserve_asn_response(self, asnreservexmlschema, responsedeletereserveasncommandxmlexpected):
        response = EppResponse.from_xml(responsedeletereserveasncommandxmlexpected,
                                        extra_nsmap={'asnReserve': 'urn:ietf:params:xml:ns:asnReserve-1.0'})
        xml = response.to_xml(force_prefix=True).decode()

        assert 'ABC-12345' == response['epp']['response']['trID']['clTRID']
        assert '54321-XYZ' == response['epp']['response']['trID']['svTRID']
        assert asnreservexmlschema.validate(etree.fromstring(xml))
