import pytest
from eppy.doc import EppResponse
from lxml import etree

from registrobrepp.common.authinfo import AuthInfo
from registrobrepp.domain.brinfodomaincommand import BrEppInfoDomainCommand
from registrobrepp.domain.eppinfobrdomain import EppInfoBrDomain
from registrobrepp.domain.eppinfolaunch import EppInfoLaunch


class TestBrInfoDomainCommand:

    @pytest.fixture
    def eppinfodomaincommand(self):
        authinfo = AuthInfo('2fooBAR')
        command = BrEppInfoDomainCommand('example.com', authinfo)
        command.add_clTRID('ABC-12345')
        return command

    def test_info_domain_command(self, eppinfodomaincommand, domainxmlschema, infodomaincommandxmlexpected):
        xml = eppinfodomaincommand.to_xml(force_prefix=True).decode()

        assert domainxmlschema.validate(etree.fromstring(xml))
        assert xml == infodomaincommandxmlexpected

    def test_info_domain_command_with_launch_extension(self, eppinfodomaincommand, infodomaincommandwithlaunchxmlexpected):
        launch = EppInfoLaunch('claims', 'abc123')
        eppinfodomaincommand.add_command_extension(launch)
        xml = eppinfodomaincommand.to_xml(force_prefix=True).decode()

        assert xml == infodomaincommandwithlaunchxmlexpected

    def test_info_domain_command_with_brdomain_extension(self, eppinfodomaincommand, infodomaincommandwithbrdomainxmlexpected):
        brdomain = EppInfoBrDomain('123456')
        eppinfodomaincommand.add_command_extension(brdomain)
        xml = eppinfodomaincommand.to_xml(force_prefix=True).decode()

        assert xml == infodomaincommandwithbrdomainxmlexpected

    def test_info_domain_response(self, domainxmlschema, responseinfodomaincommandxmlexpected):
        response = EppResponse.from_xml(responseinfodomaincommandxmlexpected)
        xml = response.to_xml(force_prefix=True).decode()
        data = response['epp']['response']['resData']['domain:infData']

        assert data.name == 'example.com'
        assert data.roid == 'EXAMPLE1-REP'
        assert data.status[0]['@s'] == 'ok'
        assert data.registrant == 'jd1234'
        assert data.contact[0]['@type'] == 'admin'
        assert data.contact[0]['_text'] == 'sh8013'
        assert data.contact[1]['@type'] == 'tech'
        assert data.contact[1]['_text'] == 'sh8013'
        assert data.ns.hostObj[0] == 'ns1.example.com'
        assert data.ns.hostObj[1] == 'ns1.example.net'
        assert data.host[0] == 'ns1.example.com'
        assert data.host[1] == 'ns2.example.com'
        assert data.clID == 'ClientX'
        assert data.crID == 'ClientY'
        assert data.crDate == '1999-04-03T22:00:00.0Z'
        assert data.upID == 'ClientX'
        assert data.upDate == '1999-12-03T09:00:00.0Z'
        assert data.exDate == '2005-04-03T22:00:00.0Z'
        assert data.trDate == '2000-04-08T09:00:00.0Z'
        assert data.authInfo.pw == '2fooBAR'
        assert response['epp']['response']['trID']['clTRID'] == 'ABC-12345'
        assert response['epp']['response']['trID']['svTRID'] == '54322-XYZ'
        assert domainxmlschema.validate(etree.fromstring(xml))
        assert xml == responseinfodomaincommandxmlexpected

    def test_info_domain_response_unauthorized_client(self, domainxmlschema, responseinfodomaincommandxmlunauthorizedclient):
        response = EppResponse.from_xml(responseinfodomaincommandxmlunauthorizedclient)
        xml = response.to_xml(force_prefix=True).decode()
        data = response['epp']['response']['resData']['domain:infData']

        assert data.name == 'example.com'
        assert data.roid == 'EXAMPLE1-REP'
        assert data.clID == 'ClientX'
        assert response['epp']['response']['trID']['clTRID'] == 'ABC-12345'
        assert response['epp']['response']['trID']['svTRID'] == '54322-XYZ'
        assert domainxmlschema.validate(etree.fromstring(xml))
        assert xml == responseinfodomaincommandxmlunauthorizedclient

    def test_info_domain_with_brdomain_response(self, responseinfodomaincommandwithbrdomainxmlexpected):
        response = EppResponse.from_xml(responseinfodomaincommandwithbrdomainxmlexpected,
                                        extra_nsmap={'brdomain': 'urn:ietf:params:xml:ns:brdomain-1.0'})
        extension = response.get_response_extension('brdomain:infData')

        assert extension.organization == '005.506.560/0001-36'
        assert extension.publicationStatus['@publicationFlag'] == 'onHold'
        assert extension.publicationStatus['onHoldReason'][0] == 'billing'
        assert extension.publicationStatus['onHoldReason'][1] == 'dns'
        assert extension.autoRenew['@active'] == '1'
        assert response['epp']['response']['trID']['clTRID'] == 'ABC-12345'
        assert response['epp']['response']['trID']['svTRID'] == '54322-XYZ'
