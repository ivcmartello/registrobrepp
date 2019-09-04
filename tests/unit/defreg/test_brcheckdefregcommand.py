import pytest
from eppy.doc import EppResponse
from lxml import etree

from registrobrepp.defreg.breppcheckdefregcommand import BrEppCheckDefRegCommand
from registrobrepp.defreg.leveltype import LevelType
from registrobrepp.defreg.namedefreg import NameDefReg


class TestBrCheckDefRegCommand:

    @pytest.fixture
    def eppcheckdefregcommand(self):
        names = [NameDefReg(LevelType.PREMIUM, 'doe'), NameDefReg(LevelType.STANDARD, 'john.doe')]
        command = BrEppCheckDefRegCommand(names)
        command.add_clTRID('ABC-12345')
        return command

    def test_check_defreg_command(self, eppcheckdefregcommand, defregxmlschema, checkdefregcommandxmlexpected):
        xml = eppcheckdefregcommand.to_xml(force_prefix=True).decode()

        assert defregxmlschema.validate(etree.fromstring(xml))
        assert xml == checkdefregcommandxmlexpected

    def test_check_defreg_response(self, responsecheckdefregcommandxmlexpected):
        response = EppResponse.from_xml(responsecheckdefregcommandxmlexpected, extra_nsmap={
            'defReg': 'http://nic.br/epp/defReg-1.0'
        })
        xml = response.to_xml(force_prefix=True).decode()
        cds = response['epp']['response']['resData']['defReg:chkData']['cd']

        assert cds[0].name['@level'] == 'premium'
        assert cds[0].name['@avail'] == '1'
        assert cds[0].name['_text'] == 'doe'
        assert cds[1].name['@level'] == 'standard'
        assert cds[1].name['@avail'] == '0'
        assert cds[1].name['_text'] == 'john.doe'
        assert cds[1].reason == 'Conflicting object exists'
        assert response['epp']['response']['trID']['clTRID'] == 'ABC-12345'
        assert response['epp']['response']['trID']['svTRID'] == '54322-XYZ'
        assert xml == responsecheckdefregcommandxmlexpected