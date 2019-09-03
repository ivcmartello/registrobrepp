import pytest
from eppy.doc import EppResponse
from lxml import etree

from registrobrepp.domain.brdeletedomaincommand import BrEppDeleteDomainCommand
from registrobrepp.domain.eppdeletelaunch import EppDeleteLaunch


class TestBrDeleteDomainCommand:

    @pytest.fixture
    def eppdeletedomaincommand(self):
        command = BrEppDeleteDomainCommand('example.com')
        command.add_clTRID('ABC-12345')
        return command

    def test_delete_domain_command(self, eppdeletedomaincommand, domainxmlschema, deletedomaincommandxmlexpected):
        xml = eppdeletedomaincommand.to_xml(force_prefix=True).decode()

        assert domainxmlschema.validate(etree.fromstring(xml))
        assert xml == deletedomaincommandxmlexpected

    def test_delete_domain_command_with_launch_extension(self, eppdeletedomaincommand, deletedomaincommandwithlaunchxmlexpected):
        launch = EppDeleteLaunch('sunrise', 'abc123')
        eppdeletedomaincommand.add_command_extension(launch)
        xml = eppdeletedomaincommand.to_xml(force_prefix=True).decode()

        assert xml == deletedomaincommandwithlaunchxmlexpected

    def test_delete_domain_response(self, domainxmlschema, responsedeletedomaincommandxmlexpected):
        response = EppResponse.from_xml(responsedeletedomaincommandxmlexpected)
        xml = response.to_xml(force_prefix=True).decode()

        assert response['epp']['response']['trID']['clTRID'] == 'ABC-12345'
        assert response['epp']['response']['trID']['svTRID'] == '54321-XYZ'
        assert domainxmlschema.validate(etree.fromstring(xml))
        assert xml == responsedeletedomaincommandxmlexpected
