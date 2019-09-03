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
        assert xml == infocontactcommandxmlexpected

    def test_info_contact_command_with_brorg_extension(self, infocontactcommand, brorgxmlschema,
                                                       infocontactcommandwithbrorgxmlexpected):
        brorg = EppInfoBrOrg('005.506.560/0001-36')
        brorgxml = brorg.to_xml(force_prefix=True).decode()
        infocontactcommand.add_command_extension(brorg)
        xml = infocontactcommand.to_xml(force_prefix=True).decode()

        assert brorgxmlschema.validate(etree.fromstring(brorgxml))
        assert xml == infocontactcommandwithbrorgxmlexpected

    def test_info_contact_response(self, contactxmlschema, responseinfocontactcommandxmlexpected):
        response = EppResponse.from_xml(responseinfocontactcommandxmlexpected)
        xml = response.to_xml(force_prefix=True).decode()
        data = response['epp']['response']['resData']['contact:infData']

        assert data.id == 'sh8013'
        assert data.roid == 'SH8013-REP'
        assert data.status[0]['@s'] == 'linked'
        assert data.status[1]['@s'] == 'clientDeleteProhibited'
        assert data.postalInfo[0]['@type'] == 'int'
        assert data.postalInfo[0].name == 'John Doe'
        assert data.postalInfo[0].org == 'Example Inc.'
        assert data.postalInfo[0].addr.street[0] == '123 Example Dr.'
        assert data.postalInfo[0].addr.street[1] == 'Suite 100'
        assert data.postalInfo[0].addr.city == 'Dulles'
        assert data.postalInfo[0].addr.sp == 'VA'
        assert data.postalInfo[0].addr.pc == '20166-6503'
        assert data.postalInfo[0].addr.cc == 'US'
        assert data.voice['@x'] == '1234'
        assert data.voice['_text'] == '+1.7035555555'
        assert data.fax == '+1.7035555556'
        assert data.email == 'jdoe@example.com'
        assert data.clID == 'ClientY'
        assert data.crID == 'ClientX'
        assert data.crDate == '1999-04-03T22:00:00.0Z'
        assert data.upID == 'ClientX'
        assert data.upDate == '1999-12-03T09:00:00.0Z'
        assert data.trDate == '2000-04-08T09:00:00.0Z'
        assert data.authInfo.pw == '2fooBAR'
        assert data.disclose['@flag'] == '0'
        assert data.disclose.voice == ''
        assert data.disclose.email == ''
        assert response['epp']['response']['trID']['clTRID'] == 'ABC-12345'
        assert response['epp']['response']['trID']['svTRID'] == '54322-XYZ'
        assert contactxmlschema.validate(etree.fromstring(xml))
        assert xml == responseinfocontactcommandxmlexpected

    def test_info_contact_with_brorg_response(self, responseinfocontactcommandwithbrorgxmlexpected):
        response = EppResponse.from_xml(
            responseinfocontactcommandwithbrorgxmlexpected, extra_nsmap={
            'brorg': 'urn:ietf:params:xml:ns:brorg-1.0',
            'lacnicorg': 'urn:ietf:params:xml:ns:lacnicorg-1.0'
        })
        brorgextension = response.get_response_extension('brorg:infData')
        lacnicorgextension = response.get_response_extension('lacnicorg:infData')

        assert brorgextension.organization == '005.506.560/0001-36'
        assert brorgextension.contact["@type"] == 'admin'
        assert brorgextension.contact["_text"] == 'fan'
        assert brorgextension.responsible == 'João Cláudio da Silva'
        assert brorgextension.proxy == 'EDS279'
        assert brorgextension.exDate == '2006-06-06T06:00:00.0Z'
        assert brorgextension.domainName[0] == 'nic.br'
        assert brorgextension.domainName[1] == 'ptt.br'
        assert brorgextension.domainName[2] == 'registro.br'
        assert brorgextension.asNumber == '64500'
        assert brorgextension.ipRange['@version'] == 'v4'
        assert brorgextension.ipRange.startAddress == '192.168.0.0'
        assert brorgextension.ipRange.endAddress == '192.168.0.255'
        assert brorgextension.suspended == 'true'
        assert lacnicorgextension.type == 'nir'
        assert lacnicorgextension.eppStatus == 'active'
        assert lacnicorgextension.eppIP[0] == '192.168.0.1'
        assert lacnicorgextension.eppIP[1] == '192.0.2.0/24'
        assert lacnicorgextension.renewalType[0] == 'member'
        assert lacnicorgextension.renewalType[1] == 'small'
        assert lacnicorgextension.renewalType[2] == 'founding-partner'
        assert lacnicorgextension.renewalDate == '2015-06-01T12:00:00.0Z'
        assert lacnicorgextension.resourcesClass == 'non-legacy-only'
        assert lacnicorgextension.password == 'abc123'
        assert lacnicorgextension.legacy == 'true'

