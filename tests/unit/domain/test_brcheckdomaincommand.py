import pytest
from eppy.doc import EppResponse
from lxml import etree

from registrobrepp.domain.brcheckdomaincommand import BrEppCheckDomainCommand
from registrobrepp.domain.eppcheckbrdomain import EppCheckBrDomain
from registrobrepp.domain.eppchecklaunch import EppCheckLaunch


class TestBrCheckDomainCommand:

    @pytest.fixture
    def eppcheckdomaincommand(self):
        names = ['du.eti.br', 'nic.br', 'registro.br']
        command = BrEppCheckDomainCommand(names)
        command.add_clTRID('ABC-12345')
        return command

    def test_check_domain_command(self, eppcheckdomaincommand, domainxmlschema, checkdomaincommandxmlexpected):
        xml = eppcheckdomaincommand.to_xml(force_prefix=True).decode()

        assert domainxmlschema.validate(etree.fromstring(xml))
        assert xml == checkdomaincommandxmlexpected

    def test_check_domain_command_with_launch_extension(self, eppcheckdomaincommand, checkdomaincommandwithlaunchxmlexpected):
        checkLaunch = EppCheckLaunch.build('claims')
        eppcheckdomaincommand.add_command_extension(checkLaunch)
        xml = eppcheckdomaincommand.to_xml(force_prefix=True).decode()

        assert xml == checkdomaincommandwithlaunchxmlexpected

    def test_check_domain_command_with_brdomain_extension(self, eppcheckdomaincommand, checkdomaincommandwithbrdomainxmlexpected):
        brdomain = EppCheckBrDomain('005.506.560/0001-36')
        eppcheckdomaincommand.add_command_extension(brdomain)
        xml = eppcheckdomaincommand.to_xml(force_prefix=True).decode()

        assert xml == checkdomaincommandwithbrdomainxmlexpected

    def test_check_domain_response(self, domainxmlschema, responsecheckdomaincommandxmlexpected):
        response = EppResponse.from_xml(responsecheckdomaincommandxmlexpected)
        xml = response.to_xml(force_prefix=True).decode()
        cds = response['epp']['response']['resData']['domain:chkData']['cd']

        assert cds[0].name['@avail'] == '1'
        assert cds[0].name['_text'] == 'example.com'
        assert cds[1].name['@avail'] == '0'
        assert cds[1].name['_text'] == 'example.net'
        assert cds[1].reason == 'In use'
        assert cds[2].name['@avail'] == '1'
        assert cds[2].name['_text'] == 'example.org'
        assert response['epp']['response']['trID']['clTRID'] == 'ABC-12345'
        assert response['epp']['response']['trID']['svTRID'] == '54322-XYZ'
        assert domainxmlschema.validate(etree.fromstring(xml))
        assert xml == responsecheckdomaincommandxmlexpected

    def test_check_domain_with_brdomain_response(self, responsecheckdomaincommandwithbrdomainxmlexpected):
        response = EppResponse.from_xml(responsecheckdomaincommandwithbrdomainxmlexpected,
                                        extra_nsmap={'brdomain': 'urn:ietf:params:xml:ns:brdomain-1.0'})
        extension = response.get_response_extension('brdomain:chkData')
        cds = extension['cd']

        assert cds[0].name == 'e-xample.net.br'
        assert cds[0].equivalentName == 'example.net.br'
        assert cds[0].organization == '043.828.151/0001-45'
        assert cds[1]['@hasConcurrent'] == '1'
        assert cds[1].name == 'example.com.br'
        assert cds[1].ticketNumber == '123456'
        assert cds[2]['@inReleaseProcess'] == '1'
        assert cds[2].name == 'example.ind.br'
        assert cds[3].name == 'example.org.br'
        assert cds[3].organization == '043.828.151/0001-45'
