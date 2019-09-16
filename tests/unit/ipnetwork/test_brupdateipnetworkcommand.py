import datetime

import pytest
from eppy.doc import EppResponse
from lxml import etree

from registrobrepp.ipnetwork.addipnetwork import AddIpNetwork
from registrobrepp.ipnetwork.aggripnetwork import AggrIpNetwork
from registrobrepp.ipnetwork.brupdateipnetworkcommand import BrEppUpdateIpNetworkCommand
from registrobrepp.ipnetwork.chgipnetwork import ChgIpNetwork
from registrobrepp.ipnetwork.contactipnetwork import ContactIpNetwork
from registrobrepp.ipnetwork.dsdata import DsData
from registrobrepp.ipnetwork.iprange import IpRange
from registrobrepp.ipnetwork.remipnetwork import RemIpNetwork


class TestBrUpdateIpNetworkCommand:

    @pytest.fixture
    def ipnetworkcommand(self):
        roid = 'b_123456-LACNIC'
        creationdate = datetime.datetime(2011, 1, 27, 00, 00, 00)
        dsdata = DsData(IpRange('192.168.16.0', '192.168.16.255'), '12345', 3, 1, '49FD46E6C4B45C55D4AC')
        contact = ContactIpNetwork.build('AAA1', tech=True)
        add = AddIpNetwork(dsdata=[dsdata], contact=[contact])
        contact = ContactIpNetwork.build('AAA1')
        rem = RemIpNetwork([dsdata], [contact])
        organization = 'BR-DEF-LACNIC'
        alloctype = 'assignment'
        asn = 2
        chg = ChgIpNetwork(organization, alloctype, asn)
        aggr = AggrIpNetwork(roid, ['a.a.com'])

        command = BrEppUpdateIpNetworkCommand(roid, creationdate, add, rem, chg, aggr)
        command.add_clTRID('ABC-12345')
        return command

    def test_update_ipnetwork_command(self, ipnetworkcommand, ipnetworkxmlschema, updateipnetworkcommandxmlexpected):
        xml = ipnetworkcommand.to_xml(force_prefix=True).decode()

        assert ipnetworkxmlschema.validate(etree.fromstring(xml))
        assert xml == updateipnetworkcommandxmlexpected

    def test_update_ipnetwork_command_without_add_rem_chg(self):
        roid = 'b_123456-LACNIC'
        with pytest.raises(ValueError, match='At least one <ipnetwork:add>, <ipnetwork:rem>, or <ipnetwork:chg> element MUST be provided'):
            BrEppUpdateIpNetworkCommand(roid)

    def test_check_ipnetwork_response(self, responseupdateipnetworkcommandxmlexpected):
        response = EppResponse.from_xml(responseupdateipnetworkcommandxmlexpected, extra_nsmap={
            'ipnetwork': 'urn:ietf:params:xml:ns:ipnetwork-1.0'
        })
        xml = response.to_xml(force_prefix=True).decode()

        assert response['epp']['response']['trID']['clTRID'] == 'ABC-12345'
        assert response['epp']['response']['trID']['svTRID'] == '54321-XYZ'
        assert xml == responseupdateipnetworkcommandxmlexpected