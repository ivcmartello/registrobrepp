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
        xml = eppinfodomaincommand.to_xml(force_prefix=False).decode()

        assert domainxmlschema.validate(etree.fromstring(xml))
        assert infodomaincommandxmlexpected == xml

    def test_info_domain_command_with_launch_extension(self, eppinfodomaincommand, infodomaincommandwithlaunchxmlexpected):
        launch = EppInfoLaunch('claims', 'abc123')
        eppinfodomaincommand.add_command_extension(launch)
        xml = eppinfodomaincommand.to_xml(force_prefix=False).decode()

        assert infodomaincommandwithlaunchxmlexpected == xml

    def test_info_domain_command_with_brdomain_extension(self, eppinfodomaincommand, infodomaincommandwithbrdomainxmlexpected):
        brdomain = EppInfoBrDomain('123456')
        eppinfodomaincommand.add_command_extension(brdomain)
        xml = eppinfodomaincommand.to_xml(force_prefix=False).decode()

        assert infodomaincommandwithbrdomainxmlexpected == xml

    def test_info_domain_response(self, domainxmlschema, responseinfodomaincommandxmlexpected):
        response = EppResponse.from_xml(responseinfodomaincommandxmlexpected)
        xml = response.to_xml(force_prefix=False).decode()
        data = response['epp']['response']['resData']['domain:infData']

        assert 'example.com' == data['name']
        assert 'EXAMPLE1-REP' == data['roid']
        assert 'ok' == data['status'][0]['@s']
        assert 'jd1234' == data['registrant']
        assert 'admin' == data['contact'][0]['@type']
        assert 'sh8013' == data['contact'][0]['_text']
        assert 'tech' == data['contact'][1]['@type']
        assert 'sh8013' == data['contact'][1]['_text']
        assert 'ns1.example.com' == data['ns']['hostObj'][0]
        assert 'ns1.example.net' == data['ns']['hostObj'][1]
        assert 'ns1.example.com' == data['host'][0]
        assert 'ns2.example.com' == data['host'][1]
        assert 'ClientX' == data['clID']
        assert 'ClientY' == data['crID']
        assert '1999-04-03T22:00:00.0Z' == data['crDate']
        assert 'ClientX' == data['upID']
        assert '1999-12-03T09:00:00.0Z' == data['upDate']
        assert '2005-04-03T22:00:00.0Z' == data['exDate']
        assert '2000-04-08T09:00:00.0Z' == data['trDate']
        assert '2fooBAR' == data['authInfo']['pw']
        assert 'ABC-12345' == response['epp']['response']['trID']['clTRID']
        assert '54322-XYZ' == response['epp']['response']['trID']['svTRID']
        assert domainxmlschema.validate(etree.fromstring(xml))
        assert responseinfodomaincommandxmlexpected == xml

    def test_info_domain_response_unauthorized_client(self, domainxmlschema, responseinfodomaincommandxmlunauthorizedclient):
        response = EppResponse.from_xml(responseinfodomaincommandxmlunauthorizedclient)
        xml = response.to_xml(force_prefix=False).decode()
        data = response['epp']['response']['resData']['domain:infData']

        assert 'example.com' == data['name']
        assert 'EXAMPLE1-REP' == data['roid']
        assert 'ClientX' == data['clID']
        assert 'ABC-12345' == response['epp']['response']['trID']['clTRID']
        assert '54322-XYZ' == response['epp']['response']['trID']['svTRID']
        assert domainxmlschema.validate(etree.fromstring(xml))
        assert responseinfodomaincommandxmlunauthorizedclient == xml

    def test_info_domain_with_brdomain_response(self, responseinfodomaincommandwithbrdomainxmlexpected):
        response = EppResponse.from_xml(responseinfodomaincommandwithbrdomainxmlexpected,
                                        extra_nsmap={'brdomain': 'urn:ietf:params:xml:ns:brdomain-1.0'})
        extension = response.get_response_extension('brdomain:infData')

        assert '005.506.560/0001-36' == extension['organization']
        assert 'onHold' == extension['publicationStatus']['@publicationFlag']
        assert 'billing' in extension['publicationStatus']['onHoldReason']
        assert 'dns' in extension['publicationStatus']['onHoldReason']
        assert '1' == extension['autoRenew']['@active']
        assert 'ABC-12345' == response['epp']['response']['trID']['clTRID']
        assert '54322-XYZ' == response['epp']['response']['trID']['svTRID']
