import datetime

import pytest
from eppy.doc import EppResponse
from lxml import etree

from registrobrepp.common.authinfo import AuthInfo
from registrobrepp.defreg.breppcreatedefregcommand import BrEppCreateDefRegCommand
from registrobrepp.defreg.leveltype import LevelType
from registrobrepp.defreg.namedefreg import NameDefReg


class TestBrCreateDefRegCommand:

    @pytest.fixture
    def eppcreatedefregcommand(self):
        name = NameDefReg(LevelType.PREMIUM, 'doe')
        registrant = 'jd1234'
        tm = 'XYZ-123'
        tmcountry = 'US'
        tmdate = datetime.date(1990, 4, 3)
        admincontact = 'sh8013'
        authinfo = AuthInfo('abc123', 'SH8013-REP')
        command = BrEppCreateDefRegCommand(name, registrant, tm, tmcountry, tmdate, admincontact, authinfo)
        command.add_clTRID('ABC-12345')
        return command

    def test_create_defreg_command(self, eppcreatedefregcommand, defregxmlschema, createdefregcommandxmlexpected):
        xml = eppcreatedefregcommand.to_xml(force_prefix=True).decode()

        assert defregxmlschema.validate(etree.fromstring(xml))
        assert xml == createdefregcommandxmlexpected

    def test_create_defreg_response(self, responsecreatedefregcommandxmlexpected):
        response = EppResponse.from_xml(responsecreatedefregcommandxmlexpected, extra_nsmap={
            'defReg': 'http://nic.br/epp/defReg-1.0'
        })
        xml = response.to_xml(force_prefix=True).decode()
        data = response['epp']['response']['resData']['defReg:creData']

        assert data.roid == 'EXAMPLE1-REP'
        assert data.name['@level'] == 'premium'
        assert data.name['_text'] == 'doe'
        assert data.crDate == '1999-04-03T22:00:00.0Z'
        assert data.exDate == '2000-04-03T22:00:00.0Z'
        assert response['epp']['response']['trID']['clTRID'] == 'ABC-12345'
        assert response['epp']['response']['trID']['svTRID'] == '54322-XYZ'
        assert xml == responsecreatedefregcommandxmlexpected
