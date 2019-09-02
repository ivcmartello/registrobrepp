from eppy.doc import EppResponse
from lxml import etree

from registrobrepp.asn.brtransferasncommand import BrEppTransferAsnCommand


class TestBrTransferReserveAsnCommand:

    def test_transfer_request_asn_command(self, asnxmlschema, transferrequestasncommandxmlexpected):
        number = 64500
        command = BrEppTransferAsnCommand('request', number)
        command.add_clTRID('ABC-12345')
        xml = command.to_xml(force_prefix=True).decode()

        assert asnxmlschema.validate(etree.fromstring(xml))
        assert transferrequestasncommandxmlexpected == xml

    def test_transfer_request_asn_response(self, asnxmlschema, responsetransferrequestasncommandxmlexpected):
        response = EppResponse.from_xml(responsetransferrequestasncommandxmlexpected,
                                        extra_nsmap={'asn': 'urn:ietf:params:xml:ns:asn-1.0'})
        xml = response.to_xml(force_prefix=True).decode()
        data = response['epp']['response']['resData']['asn:trnData']

        assert '64500' == data.number
        assert 'pending' == data.trStatus
        assert 'ClientX' == data.reID
        assert '2000-06-08T22:00:00.0Z' == data.reDate
        assert 'ClientY' == data.acID
        assert '2000-06-13T22:00:00.0Z' == data.acDate
        assert 'ABC-12345' == response['epp']['response']['trID']['clTRID']
        assert '54322-XYZ' == response['epp']['response']['trID']['svTRID']
        assert asnxmlschema.validate(etree.fromstring(xml))
