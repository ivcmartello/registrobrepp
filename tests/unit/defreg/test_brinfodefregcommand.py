import pytest
from eppy.doc import EppResponse
from lxml import etree

from registrobrepp.common.authinfo import AuthInfo
from registrobrepp.defreg.brinfodefregcommand import BrEppInfoDefRegCommand


class TestBrInfoDefRegCommand:

    @pytest.fixture
    def eppinfodefregcommand(self):
        roid = 'EXAMPLE1-REP'
        authinfo = AuthInfo('abc123', 'SH8013-REP')
        command = BrEppInfoDefRegCommand(roid, authinfo)
        command.add_clTRID('ABC-12345')
        return command

    def test_info_defreg_command(self, eppinfodefregcommand, defregxmlschema, infodefregcommandxmlexpected):
        xml = eppinfodefregcommand.to_xml(force_prefix=True).decode()

        assert defregxmlschema.validate(etree.fromstring(xml))
        assert xml == infodefregcommandxmlexpected

    def test_info_defreg_response(self, responseinfodefregcommandxmlexpected):
        response = EppResponse.from_xml(responseinfodefregcommandxmlexpected, extra_nsmap={
            'defReg': 'http://nic.br/epp/defReg-1.0'
        })
        data = response['epp']['response']['resData']['defReg:infData']
        xml = response.to_xml(force_prefix=True).decode()

        assert data.roid == 'EXAMPLE1-REP'
        assert data.name['@level'] == 'premium'
        assert data.name['_text'] == 'doe'
        assert data.registrant == 'jd1234'
        assert data.tm == 'XYZ-123'
        assert data.tmCountry == 'US'
        assert data.tmDate == '1990-04-03'
        assert data.adminContact == 'sh8013'
        assert data.status['@s'] == 'ok'
        assert data.clID == 'ClientX'
        assert data.crID == 'ClientY'
        assert data.crDate == '1999-04-03T22:00:00.0Z'
        assert data.upID == 'ClientX'
        assert data.upDate == '1999-12-03T09:00:00.0Z'
        assert data.exDate == '2000-04-03T22:00:00.0Z'
        assert data.trDate == '2000-01-08T09:00:00.0Z'
        assert data.authInfo.pw == '2fooBAR'
        assert response['epp']['response']['trID']['clTRID'] == 'ABC-12345'
        assert response['epp']['response']['trID']['svTRID'] == '54322-XYZ'
        assert xml == responseinfodefregcommandxmlexpected
