import pytest
from eppy.doc import EppResponse
from lxml import etree

from registrobrepp.ipnetwork.breppdeleteipnetworkcommand import BrEppDeleteIpNetworkCommand


class TestBrDeleteIpNetworkCommand:

    @pytest.fixture
    def ipnetworkcommand(self):
        roid = 'b_123456-LACNIC'
        command = BrEppDeleteIpNetworkCommand(roid)
        command.add_clTRID('ABC-12345')
        return command

    def test_delete_ipnetwork_command(self, ipnetworkcommand, ipnetworkxmlschema, deleteipnetworkcommandxmlexpected):
        xml = ipnetworkcommand.to_xml(force_prefix=True).decode()

        assert ipnetworkxmlschema.validate(etree.fromstring(xml))
        assert xml == deleteipnetworkcommandxmlexpected

    def test_delete_ipnetwork_response(self, responsedeleteipnetworkcommandxmlexpected):
        response = EppResponse.from_xml(responsedeleteipnetworkcommandxmlexpected, extra_nsmap={
            'ipnetwork': 'urn:ietf:params:xml:ns:ipnetwork-1.0'
        })
        xml = response.to_xml(force_prefix=True).decode()

        assert response['epp']['response']['trID']['clTRID'] == 'ABC-12345'
        assert response['epp']['response']['trID']['svTRID'] == '54321-XYZ'
        assert xml == responsedeleteipnetworkcommandxmlexpected
