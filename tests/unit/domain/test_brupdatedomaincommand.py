import datetime

import pytest
from eppy.doc import EppResponse
from lxml import etree

from registrobrepp.common.authinfo import AuthInfo
from registrobrepp.common.language import Language
from registrobrepp.common.statustype import StatusDomainType
from registrobrepp.domain.chgbrdomain import ChgBrDomain
from registrobrepp.domain.contactdomain import ContactDomain
from registrobrepp.domain.brupdatedomaincommand import ChgDomain, BrEppUpdateDomainCommand, AddDomain, RemDomain
from registrobrepp.domain.eppupdatebrdomain import EppUpdateBrDomain
from registrobrepp.domain.eppupdatelaunch import EppUpdateLaunch
from registrobrepp.domain.eppupdatergp import EppUpdateRgp
from registrobrepp.domain.eppupdatesecdns import EppUpdateSecDns
from registrobrepp.domain.nshostobj import NsHostObj
from registrobrepp.domain.publicationstatus import PublicationStatus
from registrobrepp.domain.statement import Statement
from registrobrepp.common.status import StatusDomain


class TestBrUpdateDomainCommand:

    @pytest.fixture
    def updatedomaincommand(self):
        authinfo = AuthInfo('2BARfoo')
        ns = NsHostObj(['ns2.example.com'])
        contact = ContactDomain.build(info='mak21', tech=True)
        statusadd = StatusDomain(StatusDomainType.CLIENTHOLD, 'Payment overdue.', Language.EN)
        add = AddDomain(ns, contact, statusadd)
        ns = NsHostObj(['ns1.example.com'])
        contact = ContactDomain.build(info='sh8013', tech=True)
        statusrem = StatusDomain(StatusDomainType.CLIENTUPDATEPROHIBITED)
        rem = RemDomain(ns, contact, statusrem)
        chg = ChgDomain('sh8013', authinfo)
        command = BrEppUpdateDomainCommand('example.com', add, rem, chg)
        command.add_clTRID('ABC-12345')
        return command

    def test_update_domain_command(self, updatedomaincommand, domainxmlschema, updatedomaincommandxmlexpected):
        xml = updatedomaincommand.to_xml(force_prefix=True).decode()

        assert domainxmlschema.validate(etree.fromstring(xml))
        assert xml == updatedomaincommandxmlexpected

    def test_update_domain_command_with_secdns_extension(self, updatedomaincommand, updatedomaincommandwithsecdnsxmlexpected):
        secdns = EppUpdateSecDns('12346', 3, 1, '38EC35D5B3A34B44C39B')
        updatedomaincommand.add_command_extension(secdns)
        xml = updatedomaincommand.to_xml(force_prefix=True).decode()

        assert xml == updatedomaincommandwithsecdnsxmlexpected

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
        xml = updatedomaincommand.to_xml(force_prefix=True).decode()

        assert xml == updatedomaincommandwithrgpxmlexpected

    def test_update_domain_command_with_launch_extension(self, updatedomaincommand, updatedomaincommandwithlaunchxmlexpected):
        launch = EppUpdateLaunch('sunrise', 'abc123')
        updatedomaincommand.add_command_extension(launch)
        xml = updatedomaincommand.to_xml(force_prefix=True).decode()

        assert xml == updatedomaincommandwithlaunchxmlexpected

    def test_update_domain_command_with_brdomain_extension(self, updatedomaincommandwithbrdomainxmlexpected):
        brdomain = EppUpdateBrDomain('ab-1234', chg=ChgBrDomain(flag1=1, publicationstatus=PublicationStatus.ONHOLD,
                                                                autorenew=True))
        updatedomaincommand = BrEppUpdateDomainCommand('teste.com.br')
        updatedomaincommand.add_command_extension(brdomain)
        xml = updatedomaincommand.to_xml(force_prefix=True).decode()

        assert xml == updatedomaincommandwithbrdomainxmlexpected

    def test_update_domain_response(self, domainxmlschema, responseupdatedomaincommandxmlexpected):
        response = EppResponse.from_xml(responseupdatedomaincommandxmlexpected)
        xml = response.to_xml(force_prefix=True).decode()

        assert response['epp']['response']['trID']['clTRID'] == 'ABC-12345'
        assert response['epp']['response']['trID']['svTRID'] == '54321-XYZ'
        assert domainxmlschema.validate(etree.fromstring(xml))
        assert xml == responseupdatedomaincommandxmlexpected

    def test_update_domain_with_brdomain_case1_response(self, responseupdatedomaincommandwithbrdomainxmlexpected_case1):
        response = EppResponse.from_xml(responseupdatedomaincommandwithbrdomainxmlexpected_case1,
                                        extra_nsmap={'brdomain': 'urn:ietf:params:xml:ns:brdomain-1.0'})
        extension = response.get_response_extension('brdomain:updData')

        assert extension['ticketNumber'] == '123456'
        assert extension['pending']['doc']['@status'] == 'notReceived'
        assert extension['pending']['doc']['docType'] == 'CNPJ'
        assert extension['pending']['doc']['limit'] == '2006-03-01T22:00:00.0Z'
        assert extension['pending']['doc']['description']['@lang'] == 'pt'
        assert extension['pending']['doc']['description']['_text'] == 'Cadastro Nacional da Pessoa Juridica'
        assert response['epp']['response']['trID']['clTRID'] == 'ABC-12345'
        assert response['epp']['response']['trID']['svTRID'] == '54321-XYZ'

    def test_update_domain_with_brdomain_case2_response(self, responseupdatedomaincommandwithbrdomainxmlexpected_case2):
        response = EppResponse.from_xml(responseupdatedomaincommandwithbrdomainxmlexpected_case2,
                                        extra_nsmap={'brdomain': 'urn:ietf:params:xml:ns:brdomain-1.0'})
        extension = response.get_response_extension('brdomain:updData')

        assert extension['hostStatus']['hostName'] == 'ns2.example.com'
        assert extension['hostStatus']['dnsAnswer'] == 'Query refused'
        assert extension['publicationStatus']['@publicationFlag'] == 'onHold'
        assert extension['publicationStatus']['onHoldReason'][0] == 'billing'
        assert extension['publicationStatus']['onHoldReason'][1] == 'dns'
        assert response['epp']['response']['trID']['clTRID'] == 'ABC-12345'
        assert response['epp']['response']['trID']['svTRID'] == '54321-XYZ'
