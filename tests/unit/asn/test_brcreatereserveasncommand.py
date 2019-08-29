from eppy.doc import EppResponse
from lxml import etree

from registrobrepp.asn.brcreatereserveasncommand import BrEppCreateReserveAsnCommand


class TestBrCreateReserveAsnCommand:

    def test_create_reserve_asn_command(self, asnreservexmlschema, createreserveasncommandxmlexpected):
        startAsn = 65536
        endAsn = 131072
        organization = 'BR-ABCD-LACNIC'
        comment = 'Test Reservation'
        command = BrEppCreateReserveAsnCommand(startAsn, endAsn, organization, comment)
        command.add_clTRID('ABC-12345')
        xml = command.to_xml(force_prefix=False).decode()

        assert asnreservexmlschema.validate(etree.fromstring(xml))
        assert createreserveasncommandxmlexpected == xml

    def test_create_reserve_asn_response(self, asnreservexmlschema, responsecreatereserveasncommandxmlexpected):
        response = EppResponse.from_xml(responsecreatereserveasncommandxmlexpected,
                                        extra_nsmap={'asnReserve': 'urn:ietf:params:xml:ns:asnReserve-1.0'})
        xml = response.to_xml(force_prefix=False).decode()
        data = response['epp']['response']['resData']['asnReserve:creData']

        assert '1024' == data['id']
        assert '1999-04-03T22:00:00.0Z' == data['crDate']
        assert 'ABC-12345' == response['epp']['response']['trID']['clTRID']
        assert '54321-XYZ' == response['epp']['response']['trID']['svTRID']
        assert asnreservexmlschema.validate(etree.fromstring(xml))
