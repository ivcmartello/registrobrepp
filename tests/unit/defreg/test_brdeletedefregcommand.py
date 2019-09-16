import pytest
from eppy.doc import EppResponse
from lxml import etree

from registrobrepp.defreg.brdeletedefregcommand import BrEppDeleteDefRegCommand


class TestBrDeleteDefRegCommand:

    @pytest.fixture
    def eppdeletedefregcommand(self):
        roid = 'EXAMPLE1-REP'
        command = BrEppDeleteDefRegCommand(roid)
        command.add_clTRID('ABC-12345')
        return command

    def test_delete_defreg_command(self, eppdeletedefregcommand, defregxmlschema, deletedefregcommandxmlexpected):
        xml = eppdeletedefregcommand.to_xml(force_prefix=True).decode()

        assert defregxmlschema.validate(etree.fromstring(xml))
        assert xml == deletedefregcommandxmlexpected

    def test_delete_defreg_response(self, responsedeletedefregcommandxmlexpected):
        response = EppResponse.from_xml(responsedeletedefregcommandxmlexpected, extra_nsmap={
            'defReg': 'http://nic.br/epp/defReg-1.0'
        })
        xml = response.to_xml(force_prefix=True).decode()

        assert response['epp']['response']['trID']['clTRID'] == 'ABC-12345'
        assert response['epp']['response']['trID']['svTRID'] == '54322-XYZ'
        assert xml == responsedeletedefregcommandxmlexpected
