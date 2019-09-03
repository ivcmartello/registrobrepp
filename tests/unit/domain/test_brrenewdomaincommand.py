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
        xml = brepprenewdomaincommand.to_xml(force_prefix=True).decode()

        assert domainxmlschema.validate(etree.fromstring(xml))
        assert xml == renewdomaincommandxmlexpected

    def test_renew_domain_response(self, domainxmlschema, responserenewdomaincommandxmlexpected):
        response = EppResponse.from_xml(responserenewdomaincommandxmlexpected)
        xml = response.to_xml(force_prefix=True).decode()
        data = response['epp']['response']['resData']['domain:renData']

        assert data.name == 'example.com'
        assert data.exDate == '2005-04-03T22:00:00.0Z'
        assert response['epp']['response']['trID']['clTRID'] == 'ABC-12345'
        assert response['epp']['response']['trID']['svTRID'] == '54322-XYZ'
        assert domainxmlschema.validate(etree.fromstring(xml))
        assert xml == responserenewdomaincommandxmlexpected

    def test_renew_domain_with_brdomain_response(self, responserenewdomaincommandwithbrdomaixmlexpected):
        response = EppResponse.from_xml(responserenewdomaincommandwithbrdomaixmlexpected,
                                        extra_nsmap={'brdomain': 'urn:ietf:params:xml:ns:brdomain-1.0'})
        extension = response.get_response_extension('brdomain:renData')
        publicationflag = extension.publicationStatus['@publicationFlag']
        reasons = extension.publicationStatus[publicationflag + 'Reason']

        assert publicationflag == 'onHold'
        assert reasons[0] == 'billing'
        assert reasons[1] == 'dns'
        assert response['epp']['response']['trID']['clTRID'] == 'ABC-12345'
        assert response['epp']['response']['trID']['svTRID'] == '54322-XYZ'
