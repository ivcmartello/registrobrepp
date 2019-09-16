import pytest
from eppy.doc import EppResponse
from lxml import etree

from registrobrepp.ipnetwork.brinfoipnetworkcommand import BrEppInfoIpNetworkCommand
from registrobrepp.ipnetwork.iprange import IpRange


class TestBrInfoIpNetworkCommand:

    @pytest.fixture
    def ipnetworkcommand(self):
        iprange = IpRange('192.168.0.0', '192.168.15.255')
        roid = 'b_123456-LACNIC'
        command = BrEppInfoIpNetworkCommand(iprange, roid)
        command.add_clTRID('ABC-12345')
        return command

    def test_info_ipnetwork_command(self, ipnetworkcommand, ipnetworkxmlschema, infoipnetworkcommandxmlexpected):
        xml = ipnetworkcommand.to_xml(force_prefix=True).decode()

        assert ipnetworkxmlschema.validate(etree.fromstring(xml))
        assert xml == infoipnetworkcommandxmlexpected

    def test_info_ipnetwork_response(self, responseinfoipnetworkcommandxmlexpected):
        response = EppResponse.from_xml(responseinfoipnetworkcommandxmlexpected, extra_nsmap={
            'ipnetwork': 'urn:ietf:params:xml:ns:ipnetwork-1.0'
        })
        xml = response.to_xml(force_prefix=True).decode()
        data = response['epp']['response']['resData']['ipnetwork:infData']

        assert data.ipRange['@version'] == 'v4'
        assert data.ipRange.startAddress == '192.168.0.0'
        assert data.ipRange.endAddress == '192.168.15.255'
        assert data.ipRangeInfo.roid == 'b_123456-LACNIC'
        assert data.ipRangeInfo.allocType == 'allocation'
        assert data.ipRangeInfo.organization == 'BR-ABC-LACNIC'
        assert data.ipRangeInfo.contact['@type'] == 'admin'
        assert data.ipRangeInfo.contact['_text'] == 'HKK'

        assert data.ipRangeInfo.reverseDNS[0].ipRange['@version'] == 'v4'
        assert data.ipRangeInfo.reverseDNS[0].ipRange.startAddress == '192.168.0.0'
        assert data.ipRangeInfo.reverseDNS[0].ipRange.endAddress == '192.168.0.255'
        assert data.ipRangeInfo.reverseDNS[0].hostName[0] == 'a.example.com'
        assert data.ipRangeInfo.reverseDNS[0].hostName[1] == 'b.example.com'

        assert data.ipRangeInfo.reverseDNS[1].ipRange['@version'] == 'v4'
        assert data.ipRangeInfo.reverseDNS[1].ipRange.startAddress == '192.168.2.0'
        assert data.ipRangeInfo.reverseDNS[1].ipRange.endAddress == '192.168.2.255'
        assert data.ipRangeInfo.reverseDNS[1].hostName[0] == 'd.example.com'
        assert data.ipRangeInfo.reverseDNS[1].hostName[1] == 'e.example.com'

        assert data.ipRangeInfo.dsData[0].ipRange['@version'] == 'v4'
        assert data.ipRangeInfo.dsData[0].ipRange.startAddress == '192.168.0.0'
        assert data.ipRangeInfo.dsData[0].ipRange.endAddress == '192.168.0.255'
        assert data.ipRangeInfo.dsData[0].keyTag == '12345'
        assert data.ipRangeInfo.dsData[0].alg == '3'
        assert data.ipRangeInfo.dsData[0].digestType == '1'
        assert data.ipRangeInfo.dsData[0].digest == '49FD46E6C4B45C55D4AC'

        assert data.ipRangeInfo.dsData[1].ipRange['@version'] == 'v4'
        assert data.ipRangeInfo.dsData[1].ipRange.startAddress == '192.168.2.0'
        assert data.ipRangeInfo.dsData[1].ipRange.endAddress == '192.168.2.255'
        assert data.ipRangeInfo.dsData[1].keyTag == '54321'
        assert data.ipRangeInfo.dsData[1].alg == '3'
        assert data.ipRangeInfo.dsData[1].digestType == '1'
        assert data.ipRangeInfo.dsData[1].digest == '49FD46E6C4B45C55D4AC'

        assert data.ipRangeInfo.parentNetwork.ipRange['@version'] == 'v4'
        assert data.ipRangeInfo.parentNetwork.ipRange.startAddress == '192.168.0.0'
        assert data.ipRangeInfo.parentNetwork.ipRange.endAddress == '192.168.255.255'
        assert data.ipRangeInfo.parentNetwork.roid == 'b_12345-LACNIC'

        assert data.ipRangeInfo.childNetwork.ipRange['@version'] == 'v4'
        assert data.ipRangeInfo.childNetwork.ipRange.startAddress == '192.168.0.0'
        assert data.ipRangeInfo.childNetwork.ipRange.endAddress == '192.168.0.127'
        assert data.ipRangeInfo.childNetwork.roid == 'b_234567-LACNIC'

        assert data.ipRangeInfo.clID == 'ClientY'
        assert data.ipRangeInfo.crID == 'ClientX'
        assert data.ipRangeInfo.crDate == '1999-04-03T22:00:00.0Z'
        assert data.ipRangeInfo.upID == 'ClientX'
        assert data.ipRangeInfo.upDate == '1999-12-03T09:00:00.0Z'

        assert response['epp']['response']['trID']['clTRID'] == 'ABC-12345'
        assert response['epp']['response']['trID']['svTRID'] == '54322-XYZ'
        assert xml == responseinfoipnetworkcommandxmlexpected
