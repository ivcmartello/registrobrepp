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
        assert xml == transferrequestasncommandxmlexpected

    def test_transfer_request_asn_response(self, asnxmlschema, responsetransferrequestasncommandxmlexpected):
        response = EppResponse.from_xml(responsetransferrequestasncommandxmlexpected,
                                        extra_nsmap={'asn': 'urn:ietf:params:xml:ns:asn-1.0'})
        xml = response.to_xml(force_prefix=True).decode()
        data = response['epp']['response']['resData']['asn:trnData']

        assert data.number == '64500'
        assert data.trStatus == 'pending'
        assert data.reID == 'ClientX'
        assert data.reDate == '2000-06-08T22:00:00.0Z'
        assert data.acID == 'ClientY'
        assert data.acDate == '2000-06-13T22:00:00.0Z'
        assert response['epp']['response']['trID']['clTRID'] == 'ABC-12345'
        assert response['epp']['response']['trID']['svTRID'] == '54322-XYZ'
        assert asnxmlschema.validate(etree.fromstring(xml))
