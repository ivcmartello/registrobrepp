import pytest
from eppy.doc import EppResponse
from lxml import etree

from registrobrepp.ipnetwork.brcheckipnetworkcommand import BrEppCheckIpNetworkCommand
from registrobrepp.ipnetwork.iprange import IpRange


class TestBrCheckIpNetworkCommand:

    @pytest.fixture
    def ipnetworkcommand(self):
        iprange = [IpRange('192.168.0.0', '192.168.0.255')]
        command = BrEppCheckIpNetworkCommand(iprange)
        command.add_clTRID('ABC-12345')
        return command

    def test_check_ipnetwork_command(self, ipnetworkcommand, ipnetworkxmlschema, checkipnetworkcommandxmlexpected):
        xml = ipnetworkcommand.to_xml(force_prefix=True).decode()

        assert ipnetworkxmlschema.validate(etree.fromstring(xml))
        assert xml == checkipnetworkcommandxmlexpected

    def test_check_ipnetwork_response(self, responsecheckipnetworkcommandxmlexpected):
        response = EppResponse.from_xml(responsecheckipnetworkcommandxmlexpected, extra_nsmap={
            'ipnetwork': 'urn:ietf:params:xml:ns:ipnetwork-1.0'
        })
        xml = response.to_xml(force_prefix=True).decode()
        cd = response['epp']['response']['resData']['ipnetwork:chkData']['cd']

        assert cd.ipRange['@avail'] == '0'
        assert cd.ipRange['@version'] == 'v4'
        assert cd.ipRange.startAddress == '192.168.0.0'
        assert cd.ipRange.endAddress == '192.168.0.255'
        assert cd.reason == 'In use'
        assert response['epp']['response']['trID']['clTRID'] == 'ABC-12345'
        assert response['epp']['response']['trID']['svTRID'] == '54322-XYZ'
        assert xml == responsecheckipnetworkcommandxmlexpected
