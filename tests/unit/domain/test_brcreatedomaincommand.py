import pytest
from eppy.doc import EppResponse
from lxml import etree

from registrobrepp.authinfo import AuthInfo
from registrobrepp.domain.brcreatedomaincommand import BrEppCreateDomainCommand
from registrobrepp.domain.contact import Contact
from registrobrepp.domain.eppcreatebrdomain import EppCreateBrDomain
from registrobrepp.domain.eppcreatelaunch import EppCreateLaunch
from registrobrepp.domain.eppcreatesecdns import EppCreateSecDns
from registrobrepp.domain.ns import Ns
from registrobrepp.domain.smd import Smd


class TestBrCreateDomainCommand:

    @pytest.fixture
    def eppcreatedomaincommand(self):
        authinfo = AuthInfo('2fooBAR')
        ns = Ns(['ns1.example.net', 'ns2.example.net'])
        contacts = [Contact.build('sh8013', admin=True), Contact.build('sh8013', tech=True), Contact.build('xxx')]
        command = BrEppCreateDomainCommand('example.com', ns, authinfo, 2, 'y', 'jd1234', contacts)
        command.add_clTRID('ABC-12345')
        return command

    def test_create_domain_command(self, eppcreatedomaincommand, domainxmlschema, createdomaincommandxmlexpected):
        xml = eppcreatedomaincommand.to_xml(force_prefix=False).decode()

        assert domainxmlschema.validate(etree.fromstring(xml))
        assert createdomaincommandxmlexpected == xml

    def test_create_domain_with_secdns_command(self, eppcreatedomaincommand, createdomaincommandwithsecdnsxmlexpected):
        secdns = EppCreateSecDns('12345', 3, 1, '49FD46E6C4B45C55D4AC')
        eppcreatedomaincommand.add_command_extension(secdns)
        xml = eppcreatedomaincommand.to_xml(force_prefix=False).decode()

        assert createdomaincommandwithsecdnsxmlexpected == xml

    def test_create_domain_with_lauch_command(self, eppcreatedomaincommand, createdomaincommandwithlaunchxmlexpected):
        smd = Smd('YkM1cFkyRnViaTV2Y21jdmRHMWphRjl3YVd4dmRDNWpjbXd3UlFZRFZSMGdCRDR3UERBNkJnTXFBd1F3TXpBeEJnZ3JCZ0VGQlFjQwpBUllsYUhSMGNEb3ZMM2QzZHk1cFkyRnViaTV2Y21jdmNHbHNiM1JmY21Wd2IzTnBkRzl5ZVRBTkJna3Foa2lHOXcwQkFRc0ZBQU9DCkFRRUFLVWZFSjVYNlFBdHRhampSVnNlSkZReFJYR0hUZ0NhRGs4Qy8xbmoxaWVsWkF1WnRnZFVwV0RVcjBObkdDaStMSFNzZ2RUWVIKK3ZNcnhpcjdFVllRZXZyQm9iRUxreGVURWZqRjlGVnFqQkhJbnlQRkxPRmt6MTV6R0cySXdQSnBzK3ZoQWQvN2dUMHBoMWsyRkVrSgpGR0w1THdSZjFtczRJWDB2RGt4VElYOFF4eTFqY3pDaVNzb1Y4cHdsaGgyTkhBa3BHUVdOL3BUUzBVcWk3dVU1Qm0vSW9HdlBCelVwCjVuNVNqVU1uVFp4LysxekF1ZXJTYWJ0NDgzc1hCY1dzamdsN01xRnRmT05pQXROZU1OZmg2MGxUTXU0emdWd0xaVE80VFFNNVEydXkKbFBQbVp0d25BODhRdk0ySUw4NWNJWUpIZDB6OWpwVVFNQkdIWEYyV1FBPT08L2RzOlg1MDlDZXJ0aWZpY2F0ZT48L2RzOlg1MDlEYXRhPjwvZHM6S2V5SW5mbz48L2RzOlNpZ25hdHVyZT48L3NtZDpzaWduZWRNYXJrPg==')
        launch = EppCreateLaunch('sunrise', smd)
        eppcreatedomaincommand.add_command_extension(launch)
        xml = eppcreatedomaincommand.to_xml(force_prefix=False).decode()

        assert createdomaincommandwithlaunchxmlexpected == xml

    def test_create_domian_with_brdomain_command(self, eppcreatedomaincommand, createdomaincommandwithbrdomainxmlexpected):
        brdomain = EppCreateBrDomain('005.506.560/0001-36', flag1='1', autorenew=True)
        eppcreatedomaincommand.add_command_extension(brdomain)
        xml = eppcreatedomaincommand.to_xml(force_prefix=False).decode()

        assert createdomaincommandwithbrdomainxmlexpected == xml

    def test_create_domain_response(self, domainxmlschema, responsecreatedomaincommandxmlexpected):
        response = EppResponse.from_xml(responsecreatedomaincommandxmlexpected)
        xml = response.to_xml(force_prefix=False).decode()
        data = response['epp']['response']['resData']['domain:creData']

        assert 'example.com' == data['name']
        assert '1999-04-03T22:00:00.0Z' == data['crDate']
        assert '2001-04-03T22:00:00.0Z' == data['exDate']
        assert 'ABC-12345' == response['epp']['response']['trID']['clTRID']
        assert '54321-XYZ' == response['epp']['response']['trID']['svTRID']
        assert domainxmlschema.validate(etree.fromstring(xml))
        assert responsecreatedomaincommandxmlexpected == xml

    def test_create_domain_with_brdomain_response(self, responsecreatedomaincommandwithbrdomaixmlexpected):
        response = EppResponse.from_xml(responsecreatedomaincommandwithbrdomaixmlexpected,
                                        extra_nsmap={'brdomain': 'urn:ietf:params:xml:ns:brdomain-1.0'})
        extension = response.get_response_extension('brdomain:creData')

        assert '123456' == extension['ticketNumber']
        assert 'notReceived' == extension['pending']['doc']['@status']
        assert 'CNPJ' == extension['pending']['doc']['docType']
        assert '2006-03-01T22:00:00.0Z' == extension['pending']['doc']['limit']
        assert 'pt' == extension['pending']['doc']['description']['@lang']
        assert 'Cadastro Nacional da Pessoa Juridica' == extension['pending']['doc']['description']['_text']
        assert 'queryTimeOut' == extension['pending']['dns']['@status']
        assert 'ns1.example.com.br' == extension['pending']['dns']['hostName']
        assert '2006-02-13T22:00:00.0Z' == extension['pending']['dns']['limit']
        assert '123451' in extension['ticketNumberConc']
        assert '123455' in extension['ticketNumberConc']
        assert 'ABC-12345' == response['epp']['response']['trID']['clTRID']
        assert '54321-XYZ' == response['epp']['response']['trID']['svTRID']
