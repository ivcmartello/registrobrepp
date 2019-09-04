import datetime

import pytest
from eppy.doc import EppResponse
from lxml import etree

from registrobrepp.common.authinfo import AuthInfo
from registrobrepp.common.language import Language
from registrobrepp.common.status import StatusDefReg
from registrobrepp.common.statustype import StatusDefRegType
from registrobrepp.defreg.adddefreg import AddDefReg
from registrobrepp.defreg.breppupdatedefregcommand import BrEppUpdateDefRegCommand
from registrobrepp.defreg.chgdefreg import ChgDefReg
from registrobrepp.defreg.remdefreg import RemDefReg


class TestBrUpdateDefRegCommand:

    @pytest.fixture
    def eppupdatedefregcommand(self):
        roid = 'EXAMPLE1-REP'
        add = AddDefReg([StatusDefReg(StatusDefRegType.CLIENTDELETEPROHIBITED, 'Deletions not desired.', Language.EN)])
        rem = RemDefReg([StatusDefReg(StatusDefRegType.CLIENTUPDATEPROHIBITED)])
        registrant = 'sh8013'
        tm = 'XYZ-123'
        tmcountry = 'US'
        tmdate = datetime.date(1990, 4, 3)
        admincontact = 'sh8013'
        authinfo = AuthInfo('abc123', 'SH8013-REP')
        chg = ChgDefReg(registrant, tm, tmcountry, tmdate, admincontact, authinfo)
        command = BrEppUpdateDefRegCommand(roid, add, rem, chg)
        command.add_clTRID('ABC-12345')
        return command

    def test_update_defreg_command(self, eppupdatedefregcommand, defregxmlschema, updatedefregcommandxmlexpected):
        xml = eppupdatedefregcommand.to_xml(force_prefix=True).decode()

        assert defregxmlschema.validate(etree.fromstring(xml))
        assert xml == updatedefregcommandxmlexpected

    def test_renew_defreg_response(self, responseupdatedefregcommandxmlexpected):
        response = EppResponse.from_xml(responseupdatedefregcommandxmlexpected, extra_nsmap={
            'defReg': 'http://nic.br/epp/defReg-1.0'
        })
        xml = response.to_xml(force_prefix=True).decode()

        assert response['epp']['response']['trID']['clTRID'] == 'ABC-12345'
        assert response['epp']['response']['trID']['svTRID'] == '54322-XYZ'
        assert xml == responseupdatedefregcommandxmlexpected