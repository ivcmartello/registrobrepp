import datetime

import pytest
from eppy.doc import EppResponse
from lxml import etree

from registrobrepp.common.periodtype import PeriodType
from registrobrepp.defreg.brepprenewdefregcommand import BrEppRenewDefRegCommand


class TestBrRenewDefRegCommand:

    @pytest.fixture
    def epprenewdefregcommand(self):
        roid = 'EXAMPLE1-REP'
        curexpdate = datetime.date(2000, 4, 3)
        period = 1
        command = BrEppRenewDefRegCommand(roid, curexpdate, period, PeriodType.YEAR)
        command.add_clTRID('ABC-12345')
        return command

    def test_renew_defreg_command(self, epprenewdefregcommand, defregxmlschema, renewdefregcommandxmlexpected):
        xml = epprenewdefregcommand.to_xml(force_prefix=True).decode()

        assert defregxmlschema.validate(etree.fromstring(xml))
        assert xml == renewdefregcommandxmlexpected

    def test_renew_defreg_response(self, responserenewdefregcommandxmlexpected):
        response = EppResponse.from_xml(responserenewdefregcommandxmlexpected, extra_nsmap={
            'defReg': 'http://nic.br/epp/defReg-1.0'
        })
        data = response['epp']['response']['resData']['defReg:renData']
        xml = response.to_xml(force_prefix=True).decode()

        assert data.roid == 'EXAMPLE1-REP'
        assert data.exDate == '2001-04-03T22:00:00.0Z'
        assert response['epp']['response']['trID']['clTRID'] == 'ABC-12345'
        assert response['epp']['response']['trID']['svTRID'] == '54322-XYZ'
        assert xml == responserenewdefregcommandxmlexpected
