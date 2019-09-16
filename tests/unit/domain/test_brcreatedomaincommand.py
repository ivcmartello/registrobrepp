import pytest
from eppy.doc import EppResponse
from lxml import etree

from registrobrepp.common.authinfo import AuthInfo
from registrobrepp.common.periodtype import PeriodType
from registrobrepp.domain.contactdomain import ContactDomain
from registrobrepp.domain.brcreatedomaincommand import BrEppCreateDomainCommand
from registrobrepp.domain.eppcreatebrdomain import EppCreateBrDomain
from registrobrepp.domain.eppcreatelaunch import EppCreateLaunch
from registrobrepp.domain.eppcreatesecdns import EppCreateSecDns
from registrobrepp.domain.hostaddr import HostAddr
from registrobrepp.domain.hostattr import HostAttr
from registrobrepp.domain.nshostatt import NsHostAtt
from registrobrepp.domain.nshostobj import NsHostObj
from registrobrepp.domain.smd import Smd


class TestBrCreateDomainCommand:

    @pytest.fixture
    def eppcreatedomaincommand(self):
        authinfo = AuthInfo('2fooBAR')
        ns = NsHostObj(['ns1.example.net', 'ns2.example.net'])
        contacts = [ContactDomain.build('sh8013', admin=True), ContactDomain.build('sh8013', tech=True),
                    ContactDomain.build('xxx')]
        command = BrEppCreateDomainCommand('example.com', ns, authinfo, 2, PeriodType.YEAR, 'jd1234', contacts)
        command.add_clTRID('ABC-12345')
        return command

    @pytest.fixture
    def eppcreatedomaincommand_with_nshostatt(self):
        authinfo = AuthInfo('2fooBAR')
        ns = NsHostAtt([HostAttr('ns1.example.com', [HostAddr('192.168.0.0')])])
        contacts = [ContactDomain.build('sh8013', admin=True), ContactDomain.build('sh8013', tech=True),
                    ContactDomain.build('xxx')]
        command = BrEppCreateDomainCommand('example.com', ns, authinfo, 2, PeriodType.YEAR, 'jd1234', contacts)
        command.add_clTRID('ABC-12345')
        return command

    def test_create_domain_command(self, eppcreatedomaincommand, domainxmlschema, createdomaincommandxmlexpected):
        xml = eppcreatedomaincommand.to_xml(force_prefix=True).decode()

        assert domainxmlschema.validate(etree.fromstring(xml))
        assert xml == createdomaincommandxmlexpected

    def test_create_domain_command_with_nshostatt(self, eppcreatedomaincommand_with_nshostatt, domainxmlschema, createdomaincommandwithnshostattxmlexpected):
        xml = eppcreatedomaincommand_with_nshostatt.to_xml(force_prefix=True).decode()

        assert domainxmlschema.validate(etree.fromstring(xml))
        assert xml == createdomaincommandwithnshostattxmlexpected

    def test_create_domain_command_with_secdns_extension(self, eppcreatedomaincommand, createdomaincommandwithsecdnsxmlexpected):
        secdns = EppCreateSecDns('12345', 3, 1, '49FD46E6C4B45C55D4AC')
        eppcreatedomaincommand.add_command_extension(secdns)
        xml = eppcreatedomaincommand.to_xml(force_prefix=True).decode()

        assert xml == createdomaincommandwithsecdnsxmlexpected

    def test_create_domain_command_with_lauch_extension(self, eppcreatedomaincommand, createdomaincommandwithlaunchxmlexpected):
        smd = Smd('YkM1cFkyRnViaTV2Y21jdmRHMWphRjl3YVd4dmRDNWpjbXd3UlFZRFZSMGdCRDR3UERBNkJnTXFBd1F3TXpBeEJnZ3JCZ0VGQlFjQwpBUllsYUhSMGNEb3ZMM2QzZHk1cFkyRnViaTV2Y21jdmNHbHNiM1JmY21Wd2IzTnBkRzl5ZVRBTkJna3Foa2lHOXcwQkFRc0ZBQU9DCkFRRUFLVWZFSjVYNlFBdHRhampSVnNlSkZReFJYR0hUZ0NhRGs4Qy8xbmoxaWVsWkF1WnRnZFVwV0RVcjBObkdDaStMSFNzZ2RUWVIKK3ZNcnhpcjdFVllRZXZyQm9iRUxreGVURWZqRjlGVnFqQkhJbnlQRkxPRmt6MTV6R0cySXdQSnBzK3ZoQWQvN2dUMHBoMWsyRkVrSgpGR0w1THdSZjFtczRJWDB2RGt4VElYOFF4eTFqY3pDaVNzb1Y4cHdsaGgyTkhBa3BHUVdOL3BUUzBVcWk3dVU1Qm0vSW9HdlBCelVwCjVuNVNqVU1uVFp4LysxekF1ZXJTYWJ0NDgzc1hCY1dzamdsN01xRnRmT05pQXROZU1OZmg2MGxUTXU0emdWd0xaVE80VFFNNVEydXkKbFBQbVp0d25BODhRdk0ySUw4NWNJWUpIZDB6OWpwVVFNQkdIWEYyV1FBPT08L2RzOlg1MDlDZXJ0aWZpY2F0ZT48L2RzOlg1MDlEYXRhPjwvZHM6S2V5SW5mbz48L2RzOlNpZ25hdHVyZT48L3NtZDpzaWduZWRNYXJrPg==')
        launch = EppCreateLaunch('sunrise', smd)
        eppcreatedomaincommand.add_command_extension(launch)
        xml = eppcreatedomaincommand.to_xml(force_prefix=True).decode()

        assert xml == createdomaincommandwithlaunchxmlexpected

    def test_create_domian_command_with_brdomain_extension(self, eppcreatedomaincommand, createdomaincommandwithbrdomainxmlexpected):
        brdomain = EppCreateBrDomain('005.506.560/0001-36', flag1='1', autorenew=True)
        eppcreatedomaincommand.add_command_extension(brdomain)
        xml = eppcreatedomaincommand.to_xml(force_prefix=True).decode()

        assert xml == createdomaincommandwithbrdomainxmlexpected

    def test_create_domain_response(self, domainxmlschema, responsecreatedomaincommandxmlexpected):
        response = EppResponse.from_xml(responsecreatedomaincommandxmlexpected)
        xml = response.to_xml(force_prefix=True).decode()
        data = response['epp']['response']['resData']['domain:creData']

        assert data.name == 'example.com'
        assert data.crDate == '1999-04-03T22:00:00.0Z'
        assert data.exDate == '2001-04-03T22:00:00.0Z'
        assert response['epp']['response']['trID']['clTRID'] == 'ABC-12345'
        assert response['epp']['response']['trID']['svTRID'] == '54321-XYZ'
        assert domainxmlschema.validate(etree.fromstring(xml))
        assert xml == responsecreatedomaincommandxmlexpected

    def test_create_domain_with_brdomain_response(self, responsecreatedomaincommandwithbrdomaixmlexpected):
        response = EppResponse.from_xml(responsecreatedomaincommandwithbrdomaixmlexpected,
                                        extra_nsmap={'brdomain': 'urn:ietf:params:xml:ns:brdomain-1.0'})
        extension = response.get_response_extension('brdomain:creData')

        assert extension.ticketNumber == '123456'
        assert extension.pending.doc['@status'] == 'notReceived'
        assert extension.pending.doc['docType'] == 'CNPJ'
        assert extension.pending.doc['limit'] == '2006-03-01T22:00:00.0Z'
        assert extension.pending.doc.description['@lang'] == 'pt'
        assert extension.pending.doc.description['_text'] == 'Cadastro Nacional da Pessoa Juridica'
        assert extension.pending.dns['@status'] == 'queryTimeOut'
        assert extension.pending.dns.hostName == 'ns1.example.com.br'
        assert extension.pending.dns.limit == '2006-02-13T22:00:00.0Z'
        assert extension.ticketNumberConc[0] == '123451'
        assert extension.ticketNumberConc[1] == '123455'
        assert response['epp']['response']['trID']['clTRID'] == 'ABC-12345'
        assert response['epp']['response']['trID']['svTRID'] == '54321-XYZ'
