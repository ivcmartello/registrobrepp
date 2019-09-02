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
        assert deletedomaincommandxmlexpected == xml

    def test_delete_domain_command_with_launch_extension(self, eppdeletedomaincommand, deletedomaincommandwithlaunchxmlexpected):
        launch = EppDeleteLaunch('sunrise', 'abc123')
        eppdeletedomaincommand.add_command_extension(launch)
        xml = eppdeletedomaincommand.to_xml(force_prefix=True).decode()

        assert deletedomaincommandwithlaunchxmlexpected == xml

    def test_delete_domain_response(self, domainxmlschema, responsedeletedomaincommandxmlexpected):
        response = EppResponse.from_xml(responsedeletedomaincommandxmlexpected)
        xml = response.to_xml(force_prefix=True).decode()

        assert 'ABC-12345' == response['epp']['response']['trID']['clTRID']
        assert '54321-XYZ' == response['epp']['response']['trID']['svTRID']
        assert domainxmlschema.validate(etree.fromstring(xml))
        assert responsedeletedomaincommandxmlexpected == xml
