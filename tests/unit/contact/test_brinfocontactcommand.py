import pytest
from eppy.doc import EppResponse
from lxml import etree

from registrobrepp.common.authinfo import AuthInfo
from registrobrepp.contact.brinfocontactcommand import BrEppInfoContactCommand
from registrobrepp.contact.eppinfobrorg import EppInfoBrOrg


class TestBrInfoContactCommand:

    @pytest.fixture
    def infocontactcommand(self):
        authinfo = AuthInfo('123')
        command = BrEppInfoContactCommand('ab-12345', authinfo)
        command.add_clTRID('ABC-12345')
        return command

    def test_info_contact_command(self, infocontactcommand, contactxmlschema, infocontactcommandxmlexpected):
        xml = infocontactcommand.to_xml(force_prefix=True).decode()

        assert contactxmlschema.validate(etree.fromstring(xml))
        assert infocontactcommandxmlexpected == xml

    def test_info_contact_command_with_brorg_extension(self, infocontactcommand, brorgxmlschema,
                                                       infocontactcommandwithbrorgxmlexpected):
        brorg = EppInfoBrOrg('005.506.560/0001-36')
        brorgxml = brorg.to_xml(force_prefix=True).decode()
        infocontactcommand.add_command_extension(brorg)
        xml = infocontactcommand.to_xml(force_prefix=True).decode()

        assert brorgxmlschema.validate(etree.fromstring(brorgxml))
        assert infocontactcommandwithbrorgxmlexpected == xml

    def test_info_contact_response(self, contactxmlschema, responseinfocontactcommandxmlexpected):
        response = EppResponse.from_xml(responseinfocontactcommandxmlexpected)
        xml = response.to_xml(force_prefix=True).decode()
        data = response['epp']['response']['resData']['contact:infData']

        assert 'sh8013' == data.id
        assert 'SH8013-REP' == data.roid
        assert 'linked' == data.status[0]['@s']
        assert 'clientDeleteProhibited' == data.status[1]['@s']
        assert 'int' == data.postalInfo[0]['@type']
        assert 'John Doe' == data.postalInfo[0].name
        assert 'Example Inc.' == data.postalInfo[0].org
        assert '123 Example Dr.' in data.postalInfo[0].addr.street
        assert 'Suite 100' in data.postalInfo[0].addr.street
        assert 'Dulles' == data.postalInfo[0].addr.city
        assert 'VA' == data.postalInfo[0].addr.sp
        assert '20166-6503' == data.postalInfo[0].addr.pc
        assert 'US' == data.postalInfo[0].addr.cc
        assert '1234' == data.voice['@x']
        assert '+1.7035555555' == data.voice['_text']
        assert '+1.7035555556' == data.fax
        assert 'jdoe@example.com' == data.email
        assert 'ClientY' == data.clID
        assert 'ClientX' == data.crID
        assert '1999-04-03T22:00:00.0Z' == data.crDate
        assert 'ClientX' == data.upID
        assert '1999-12-03T09:00:00.0Z' == data.upDate
        assert '2000-04-08T09:00:00.0Z' == data.trDate
        assert '2fooBAR' == data.authInfo.pw
        assert '0' == data.disclose['@flag']
        assert '' == data.disclose.voice
        assert '' == data.disclose.email
        assert 'ABC-12345' == response['epp']['response']['trID']['clTRID']
        assert '54322-XYZ' == response['epp']['response']['trID']['svTRID']
        assert contactxmlschema.validate(etree.fromstring(xml))
        assert responseinfocontactcommandxmlexpected == xml


    def test_info_contact_with_brorg_response(self, responseinfocontactcommandwithbrorgxmlexpected):
        response = EppResponse.from_xml(
            responseinfocontactcommandwithbrorgxmlexpected, extra_nsmap={
            'brorg': 'urn:ietf:params:xml:ns:brorg-1.0',
            'lacnicorg': 'urn:ietf:params:xml:ns:lacnicorg-1.0'
        })
        brorgextension = response.get_response_extension('brorg:infData')
        lacnicorgextension = response.get_response_extension('lacnicorg:infData')

        assert '005.506.560/0001-36' == brorgextension.organization
        assert 'admin' == brorgextension.contact["@type"]
        assert 'fan' == brorgextension.contact["_text"]
        assert 'João Cláudio da Silva' == brorgextension.responsible
        assert 'EDS279' == brorgextension.proxy
        assert '2006-06-06T06:00:00.0Z' == brorgextension.exDate
        assert 'nic.br' == brorgextension.domainName[0]
        assert 'ptt.br' == brorgextension.domainName[1]
        assert 'registro.br' == brorgextension.domainName[2]
        assert '64500' == brorgextension.asNumber
        assert 'v4' == brorgextension.ipRange['@version']
        assert '192.168.0.0' == brorgextension.ipRange.startAddress
        assert '192.168.0.255' == brorgextension.ipRange.endAddress
        assert 'true' == brorgextension.suspended

        assert 'nir' == lacnicorgextension.type
        assert 'active' == lacnicorgextension.eppStatus
        assert '192.168.0.1' == lacnicorgextension.eppIP[0]
        assert '192.0.2.0/24' == lacnicorgextension.eppIP[1]
        assert 'member' == lacnicorgextension.renewalType[0]
        assert 'small' == lacnicorgextension.renewalType[1]
        assert 'founding-partner' == lacnicorgextension.renewalType[2]
        assert '2015-06-01T12:00:00.0Z' == lacnicorgextension.renewalDate
        assert 'non-legacy-only' == lacnicorgextension.resourcesClass
        assert 'abc123' == lacnicorgextension.password
        assert 'true' == lacnicorgextension.legacy

