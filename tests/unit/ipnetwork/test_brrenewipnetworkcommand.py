import datetime

import pytest
from eppy.doc import EppResponse
from lxml import etree

from registrobrepp.ipnetwork.brepprenewipnetworkcommand import BrEppRenewIpNetworkCommand


class TestBrRenewIpNetworkCommand:

    @pytest.fixture
    def ipnetworkcommand(self):
        roid = 'b_12345-LACNIC'
        curexpdate = datetime.datetime(2008, 4, 3, 00, 00, 00)
        period = 3
        command = BrEppRenewIpNetworkCommand(roid, curexpdate, period)
        command.add_clTRID('ABC-12345')
        return command

    def test_check_ipnetwork_command(self, ipnetworkcommand, ipnetworkxmlschema, renewipnetworkcommandxmlexpected):
        xml = ipnetworkcommand.to_xml(force_prefix=True).decode()

        assert ipnetworkxmlschema.validate(etree.fromstring(xml))
        assert xml == renewipnetworkcommandxmlexpected

    def test_check_ipnetwork_response(self, responserenewipnetworkcommandxmlexpected):
        response = EppResponse.from_xml(responserenewipnetworkcommandxmlexpected, extra_nsmap={
            'ipnetwork': 'urn:ietf:params:xml:ns:ipnetwork-1.0'
        })
        xml = response.to_xml(force_prefix=True).decode()
        data = response['epp']['response']['resData']['ipnetwork:renData']

        assert data.roid == 'b_12345-LACNIC'
        assert data.exDate == '2011-04-03T00:00:00.0Z'
        assert response['epp']['response']['trID']['clTRID'] == 'ABC-12345'
        assert response['epp']['response']['trID']['svTRID'] == '54322-XYZ'
        assert xml == responserenewipnetworkcommandxmlexpected
