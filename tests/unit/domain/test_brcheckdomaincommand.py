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
        xml = eppcheckdomaincommand.to_xml(force_prefix=False).decode()

        assert domainxmlschema.validate(etree.fromstring(xml))
        assert checkdomaincommandxmlexpected == xml

    def test_check_domain_with_launch_command(self, eppcheckdomaincommand, checkdomaincommandwithlaunchxmlexpected):
        checkLaunch = EppCheckLaunch.build('claims')
        eppcheckdomaincommand.add_command_extension(checkLaunch)
        xml = eppcheckdomaincommand.to_xml(force_prefix=False).decode()

        assert checkdomaincommandwithlaunchxmlexpected == xml

    def test_check_domain_with_brdomain_command(self, eppcheckdomaincommand, checkdomaincommandwithbrdomainxmlexpected):
        brdomain = EppCheckBrDomain('005.506.560/0001-36')
        eppcheckdomaincommand.add_command_extension(brdomain)
        xml = eppcheckdomaincommand.to_xml(force_prefix=False).decode()

        assert checkdomaincommandwithbrdomainxmlexpected == xml

    def test_check_domain_response(self, domainxmlschema, responsecheckdomaincommandxmlexpected):
        response = EppResponse.from_xml(responsecheckdomaincommandxmlexpected)
        xml = response.to_xml(force_prefix=False).decode()
        cds = response['epp']['response']['resData']['domain:chkData']['cd']

        assert '1' == cds[0]['name']['@avail']
        assert 'example.com' == cds[0]['name']['_text']
        assert '0' == cds[1]['name']['@avail']
        assert 'example.net' == cds[1]['name']['_text']
        assert 'In use' == cds[1]['reason']
        assert '1' == cds[2]['name']['@avail']
        assert 'example.org' == cds[2]['name']['_text']
        assert 'ABC-12345' == response['epp']['response']['trID']['clTRID']
        assert '54322-XYZ' == response['epp']['response']['trID']['svTRID']
        assert domainxmlschema.validate(etree.fromstring(xml))
        assert responsecheckdomaincommandxmlexpected == xml

    def test_check_domain_with_brdomain_response(self, responsecheckdomaincommandwithbrdomainxmlexpected):
        response = EppResponse.from_xml(responsecheckdomaincommandwithbrdomainxmlexpected,
                                        extra_nsmap={'brdomain': 'urn:ietf:params:xml:ns:brdomain-1.0'})
        extension = response.get_response_extension('brdomain:chkData')
        cds = extension['cd']

        assert 'e-xample.net.br' == cds[0]['name']
        assert 'example.net.br' == cds[0]['equivalentName']
        assert '043.828.151/0001-45' == cds[0]['organization']
        assert '1' == cds[1]['@hasConcurrent']
        assert 'example.com.br' == cds[1]['name']
        assert '123456' == cds[1]['ticketNumber']
        assert '1' == cds[2]['@inReleaseProcess']
        assert 'example.ind.br' == cds[2]['name']
        assert 'example.org.br' == cds[3]['name']
        assert '043.828.151/0001-45' == cds[3]['organization']
