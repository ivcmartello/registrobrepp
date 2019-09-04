import pytest
from eppy.doc import EppResponse
from lxml import etree

from registrobrepp.ipnetwork.breppcreateipnetworkcommand import BrEppCreateIpNetworkCommand
from registrobrepp.ipnetwork.contactipnetwork import ContactIpNetwork
from registrobrepp.ipnetwork.dsdata import DsData
from registrobrepp.ipnetwork.iprange import IpRange
from registrobrepp.ipnetwork.reversedns import ReverseDns


class TestBrCreateIpNetworkCommand:

    @pytest.fixture
    def ipnetworkcommand(self):
        iprange = IpRange('192.168.16.0', '192.168.31.255')
        organization = 'BR-ABC-LACNIC'
        alloctype = 'assignment'
        contact = ContactIpNetwork.build('ABC123', admin=True)
        reversedns = ReverseDns(IpRange('192.168.16.0', '192.168.17.255'), ['a.example.com', 'b.example.com'])
        dsdata = DsData(IpRange('192.168.16.0', '192.168.16.255'), '12345', 3, 1, '49FD46E6C4B45C55D4AC')
        command = BrEppCreateIpNetworkCommand(iprange, organization, alloctype, contact, reversedns, dsdata)
        command.add_clTRID('ABC-12345')
        return command

    def test_create_ipnetwork_command(self, ipnetworkcommand, ipnetworkxmlschema, createipnetworkcommandxmlexpected):
        xml = ipnetworkcommand.to_xml(force_prefix=True).decode()

        assert ipnetworkxmlschema.validate(etree.fromstring(xml))
        assert xml == createipnetworkcommandxmlexpected

    def test_create_ipnetwork_response(self, responsecreateipnetworkcommandxmlexpected):
        response = EppResponse.from_xml(responsecreateipnetworkcommandxmlexpected, extra_nsmap={
            'ipnetwork': 'urn:ietf:params:xml:ns:ipnetwork-1.0'
        })
        xml = response.to_xml(force_prefix=True).decode()
        data = response['epp']['response']['resData']['ipnetwork:creData']

        assert data.ipRange['@version'] == 'v4'
        assert data.ipRange.startAddress == '192.168.16.0'
        assert data.ipRange.endAddress == '192.168.31.255'
        assert data.roid == 'b_123456-LACNIC'
        assert data.crDate == '1999-04-03T22:00:00.0Z'
        assert response['epp']['response']['trID']['clTRID'] == 'ABC-12345'
        assert response['epp']['response']['trID']['svTRID'] == '54321-XYZ'
        assert xml == responsecreateipnetworkcommandxmlexpected
