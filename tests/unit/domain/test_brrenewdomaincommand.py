import datetime
import pytest
from eppy.doc import EppResponse
from lxml import etree


from registrobrepp.domain.brrenewdomaincommand import BrEppRenewDomainCommand


class TestBrRenewDomainCommand:

    @pytest.fixture
    def brepprenewdomaincommand(self):
        curexpdate = datetime.date(2000, 4, 3)
        command = BrEppRenewDomainCommand('example.com.br', curexpdate, 5)
        command.add_clTRID('ABC-12345')
        return command

    def test_renew_domain_command(self, brepprenewdomaincommand, domainxmlschema, renewdomaincommandxmlexpected):
        xml = brepprenewdomaincommand.to_xml(force_prefix=False).decode()

        assert domainxmlschema.validate(etree.fromstring(xml))
        assert renewdomaincommandxmlexpected == xml

    def test_renew_domain_response(self, domainxmlschema, responserenewdomaincommandxmlexpected):
        response = EppResponse.from_xml(responserenewdomaincommandxmlexpected)
        xml = response.to_xml(force_prefix=False).decode()
        data = response['epp']['response']['resData']['domain:renData']

        assert 'example.com' == data['name']
        assert '2005-04-03T22:00:00.0Z' == data['exDate']
        assert 'ABC-12345' == response['epp']['response']['trID']['clTRID']
        assert '54322-XYZ' == response['epp']['response']['trID']['svTRID']
        assert domainxmlschema.validate(etree.fromstring(xml))
        assert responserenewdomaincommandxmlexpected == xml

    def test_renew_domain_with_brdomain_response(self, responserenewdomaincommandwithbrdomaixmlexpected):
        response = EppResponse.from_xml(responserenewdomaincommandwithbrdomaixmlexpected,
                                        extra_nsmap={'brdomain': 'urn:ietf:params:xml:ns:brdomain-1.0'})
        extension = response.get_response_extension('brdomain:renData')
        publicationflag = extension['publicationStatus']['@publicationFlag']
        reasons = extension['publicationStatus'][publicationflag + 'Reason']

        assert 'onHold' == publicationflag
        assert 'billing' in reasons
        assert 'dns' in reasons
        assert 'ABC-12345' == response['epp']['response']['trID']['clTRID']
        assert '54322-XYZ' == response['epp']['response']['trID']['svTRID']
