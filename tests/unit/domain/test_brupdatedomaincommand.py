import datetime

import pytest
from eppy.doc import EppResponse
from lxml import etree

from registrobrepp.common.authinfo import AuthInfo
from registrobrepp.domain.contactdomain import ContactDomain
from registrobrepp.domain.brupdatedomaincommand import ChgDomain, BrEppUpdateDomainCommand, AddDomain, RemDomain
from registrobrepp.domain.eppupdatelaunch import EppUpdateLaunch
from registrobrepp.domain.eppupdatergp import EppUpdateRgp
from registrobrepp.domain.eppupdatesecdns import EppUpdateSecDns
from registrobrepp.domain.ns import Ns
from registrobrepp.domain.statement import Statement
from registrobrepp.common.status import Status


class TestBrUpdateDomainCommand:

    @pytest.fixture
    def updatedomaincommand(self):
        authinfo = AuthInfo('2BARfoo')
        ns = Ns(['ns2.example.com'])
        contact = ContactDomain.build(info='mak21', tech=True)
        statusadd = Status(s='clientHold', lang='en', info='Payment overdue.')
        add = AddDomain(ns, contact, statusadd)
        ns = Ns(['ns1.example.com'])
        contact = ContactDomain.build(info='sh8013', tech=True)
        statusrem = Status(s='clientUpdateProhibited')
        rem = RemDomain(ns, contact, statusrem)
        chg = ChgDomain('sh8013', authinfo)
        command = BrEppUpdateDomainCommand('example.com', add, rem, chg)
        command.add_clTRID('ABC-12345')
        return command

    def test_update_domain_command(self, updatedomaincommand, domainxmlschema, updatedomaincommandxmlexpected):
        xml = updatedomaincommand.to_xml(force_prefix=False).decode()

        assert domainxmlschema.validate(etree.fromstring(xml))
        assert updatedomaincommandxmlexpected == xml

    def test_update_domain_command_with_secdns_extension(self, updatedomaincommand, updatedomaincommandwithsecdnsxmlexpected):
        secdns = EppUpdateSecDns('12346', 3, 1, '38EC35D5B3A34B44C39B')
        updatedomaincommand.add_command_extension(secdns)
        xml = updatedomaincommand.to_xml(force_prefix=False).decode()

        assert updatedomaincommandwithsecdnsxmlexpected == xml

    def test_update_domain_command_with_rgp_extension(self, updatedomaincommand, updatedomaincommandwithrgpxmlexpected):
        predata = 'Pre-delete registration data goes here. Both XML and free text are allowed.'
        postdata = 'Post-restore registration data goes here. Both XML and free text are allowed.'
        deltime = datetime.datetime(2003, 7, 10, 22, 00, 00)
        restime = datetime.datetime(2003, 7, 20, 22, 00, 00)
        resreason = 'Registrant error.'
        statement1 = 'This registrar has not restored the Registered Name in order to assume the rights to use ' \
            'or sell the Registered Name for itself or for any ' \
            'third party.'
        statement2 = 'The information in this report is ' \
            'true to best of this registrar knowledge, and this ' \
            'registrar acknowledges that intentionally supplying ' \
            'false information in this report shall constitute an ' \
            'incurable material breach of the ' \
            'Registry-Registrar Agreement.'
        other = 'Supporting information goes here.'
        st1 = Statement(statement1)
        st2 = Statement(statement2, 'en')
        rgp = EppUpdateRgp(predata, postdata, deltime, restime, resreason, [st1, st2], other)
        updatedomaincommand.add_command_extension(rgp)
        xml = updatedomaincommand.to_xml(force_prefix=False).decode()

        assert updatedomaincommandwithrgpxmlexpected == xml

    def test_update_domain_command_with_launch_extension(self, updatedomaincommand, updatedomaincommandwithlaunchxmlexpected):
        launch = EppUpdateLaunch('sunrise', 'abc123')
        updatedomaincommand.add_command_extension(launch)
        xml = updatedomaincommand.to_xml(force_prefix=False).decode()

        assert updatedomaincommandwithlaunchxmlexpected == xml

    def test_update_domain_response(self, domainxmlschema, responseupdatedomaincommandxmlexpected):
        response = EppResponse.from_xml(responseupdatedomaincommandxmlexpected)
        xml = response.to_xml(force_prefix=False).decode()

        assert 'ABC-12345' == response['epp']['response']['trID']['clTRID']
        assert '54321-XYZ' == response['epp']['response']['trID']['svTRID']
        assert domainxmlschema.validate(etree.fromstring(xml))
        assert responseupdatedomaincommandxmlexpected == xml

    def test_update_domain_with_brdomain_case1_response(self, responseupdatedomaincommandwithbrdomainxmlexpected_case1):
        response = EppResponse.from_xml(responseupdatedomaincommandwithbrdomainxmlexpected_case1,
                                        extra_nsmap={'brdomain': 'urn:ietf:params:xml:ns:brdomain-1.0'})
        extension = response.get_response_extension('brdomain:updData')

        assert '123456' == extension['ticketNumber']
        assert 'notReceived' == extension['pending']['doc']['@status']
        assert 'CNPJ' == extension['pending']['doc']['docType']
        assert '2006-03-01T22:00:00.0Z' == extension['pending']['doc']['limit']
        assert 'pt' == extension['pending']['doc']['description']['@lang']
        assert 'Cadastro Nacional da Pessoa Juridica' == extension['pending']['doc']['description']['_text']
        assert 'ABC-12345' == response['epp']['response']['trID']['clTRID']
        assert '54321-XYZ' == response['epp']['response']['trID']['svTRID']

    def test_update_domain_with_brdomain_case2_response(self, responseupdatedomaincommandwithbrdomainxmlexpected_case2):
        response = EppResponse.from_xml(responseupdatedomaincommandwithbrdomainxmlexpected_case2,
                                        extra_nsmap={'brdomain': 'urn:ietf:params:xml:ns:brdomain-1.0'})
        extension = response.get_response_extension('brdomain:updData')

        assert 'ns2.example.com' == extension['hostStatus']['hostName']
        assert 'Query refused' == extension['hostStatus']['dnsAnswer']
        assert 'onHold' == extension['publicationStatus']['@publicationFlag']
        assert 'billing' in extension['publicationStatus']['onHoldReason']
        assert 'dns' in extension['publicationStatus']['onHoldReason']
        assert 'ABC-12345' == response['epp']['response']['trID']['clTRID']
        assert '54321-XYZ' == response['epp']['response']['trID']['svTRID']
