import pytest
from eppy.doc import EppResponse
from lxml import etree

from registrobrepp.ipnetwork.brepptransferipnetworkcommand import BrEppTransferIpNetworkCommand


class TestBrTransferIpNetworkCommand:

    @pytest.fixture
    def ipnetworkcommand(self):
        roid = 'b_12345-LACNIC'
        command = BrEppTransferIpNetworkCommand('request', roid)
        command.add_clTRID('ABC-12345')
        return command

    def test_transfer_request_ipnetwork_command(self, ipnetworkcommand, ipnetworkxmlschema, transferrequestipnetworkcommandxmlexpected):
        xml = ipnetworkcommand.to_xml(force_prefix=True).decode()

        assert ipnetworkxmlschema.validate(etree.fromstring(xml))
        assert xml == transferrequestipnetworkcommandxmlexpected

    def test_check_ipnetwork_response(self, responsetransferipnetworkcommandxmlexpected):
        response = EppResponse.from_xml(responsetransferipnetworkcommandxmlexpected, extra_nsmap={
            'ipnetwork': 'urn:ietf:params:xml:ns:ipnetwork-1.0'
        })
        xml = response.to_xml(force_prefix=True).decode()
        data = response['epp']['response']['resData']['ipnetwork:trnData']

        assert data.roid == 'b_12345-LACNIC'
        assert data.trStatus == 'pending'
        assert data.reID == 'ClientX'
        assert data.reDate == '2000-06-08T22:00:00.0Z'
        assert data.acID == 'ClientY'
        assert data.acDate == '2000-06-13T22:00:00.0Z'
        assert response['epp']['response']['trID']['clTRID'] == 'ABC-12345'
        assert response['epp']['response']['trID']['svTRID'] == '54322-XYZ'
        assert xml == responsetransferipnetworkcommandxmlexpected
