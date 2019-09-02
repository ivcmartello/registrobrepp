from eppy.doc import EppResponse
from lxml import etree

from registrobrepp.common.authinfo import AuthInfo
from registrobrepp.domain.brtransferdomaincommand import BrEppTransferDomainCommand


class TestBrTransferDomainCommand:

    def test_transfer_domain_query_command(self, domainxmlschema, transferquerydomaincommandxmlexpected):
        authinfo = AuthInfo('2fooBAR', roid='JD1234-REP')
        command = BrEppTransferDomainCommand('query', 'example.com', authinfo)
        command.add_clTRID('ABC-12345')
        xml = command.to_xml(force_prefix=True).decode()

        assert domainxmlschema.validate(etree.fromstring(xml))
        assert transferquerydomaincommandxmlexpected == xml

    def test_transfer_domain_query_response(self, domainxmlschema, responsetransferquerydomaincommandxmlexpected):
        response = EppResponse.from_xml(responsetransferquerydomaincommandxmlexpected)
        xml = response.to_xml(force_prefix=True).decode()

        assert domainxmlschema.validate(etree.fromstring(xml))
        assert responsetransferquerydomaincommandxmlexpected == xml

    def test_transfer_domain_request_command(self, domainxmlschema, transferrequestdomaincommandxmlexpected):
        authinfo = AuthInfo('2fooBAR', roid='JD1234-REP')
        command = BrEppTransferDomainCommand('request', 'example.com', authinfo, period=1)
        command.add_clTRID('ABC-12345')
        xml = command.to_xml(force_prefix=True).decode()

        assert domainxmlschema.validate(etree.fromstring(xml))
        assert transferrequestdomaincommandxmlexpected == xml

    def test_transfer_domain_request_response(self, domainxmlschema, responsetransferrequestdomaincommandxmlexpected):
        response = EppResponse.from_xml(responsetransferrequestdomaincommandxmlexpected)
        xml = response.to_xml(force_prefix=True).decode()

        assert domainxmlschema.validate(etree.fromstring(xml))
        assert responsetransferrequestdomaincommandxmlexpected == xml
