import pytest
from eppy.doc import EppResponse
from lxml import etree

from registrobrepp.common.authinfo import AuthInfo
from registrobrepp.defreg.brepptransferdefregcommand import BrEppTransferDefRegCommand


class TestBrTransferDefRegCommand:

    @pytest.fixture
    def epptransferquerydefregcommand(self):
        roid = 'EXAMPLE1-REP'
        authinfo = AuthInfo('abc123', 'SH8013-REP')
        command = BrEppTransferDefRegCommand('query', roid, authinfo)
        command.add_clTRID('ABC-12345')
        return command

    def test_transfer_query_defreg_command(self, epptransferquerydefregcommand, defregxmlschema, transferquerydefregcommandxmlexpected):
        xml = epptransferquerydefregcommand.to_xml(force_prefix=True).decode()

        assert defregxmlschema.validate(etree.fromstring(xml))
        assert xml == transferquerydefregcommandxmlexpected

    def test_renew_defreg_response(self, responsetransferquerydefregcommandxmlexpected):
        response = EppResponse.from_xml(responsetransferquerydefregcommandxmlexpected, extra_nsmap={
            'defReg': 'http://nic.br/epp/defReg-1.0'
        })
        data = response['epp']['response']['resData']['defReg:trnData']
        xml = response.to_xml(force_prefix=True).decode()

        assert data.roid == 'EXAMPLE1-REP'
        assert data.trStatus == 'pending'
        assert data.reID == 'ClientX'
        assert data.reDate == '2000-06-06T22:00:00.0Z'
        assert data.acID == 'ClientY'
        assert data.acDate == '2000-06-11T22:00:00.0Z'
        assert data.exDate == '2002-09-08T22:00:00.0Z'
        assert response['epp']['response']['trID']['clTRID'] == 'ABC-12345'
        assert response['epp']['response']['trID']['svTRID'] == '54322-XYZ'
        assert xml == responsetransferquerydefregcommandxmlexpected