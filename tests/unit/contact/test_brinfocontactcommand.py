from eppy.doc import EppResponse
from lxml import etree

from registrobrepp.authinfo import AuthInfo
from registrobrepp.contact.brinfocontactcommand import BrEppInfoContactCommand


class TestBrInfoContactCommand:

    def test_info_contact_command(self, contactxmlschema, infocontactcommandxmlexpected):
        authinfo = AuthInfo('123')
        command = BrEppInfoContactCommand('ab-12345', authinfo)
        command.add_clTRID('ABC-12345')
        xml = command.to_xml(force_prefix=False).decode()

        assert contactxmlschema.validate(etree.fromstring(xml))
        assert infocontactcommandxmlexpected == xml

    def test_info_contact_response(self, contactxmlschema, responseinfocontactcommandxmlexpected):
        response = EppResponse.from_xml(responseinfocontactcommandxmlexpected)
        xml = response.to_xml(force_prefix=False).decode()
        data = response['epp']['response']['resData']['contact:infData']

        assert 'sh8013' == data['id']
        assert 'SH8013-REP' == data['roid']
        assert 'linked' == data['status'][0]['@s']
        assert 'clientDeleteProhibited' == data['status'][1]['@s']
        assert 'int' == data['postalInfo'][0]['@type']
        assert 'John Doe' == data['postalInfo'][0]['name']
        assert 'Example Inc.' == data['postalInfo'][0]['org']
        assert '123 Example Dr.' in data['postalInfo'][0]['addr']['street']
        assert 'Suite 100' in data['postalInfo'][0]['addr']['street']
        assert 'Dulles' == data['postalInfo'][0]['addr']['city']
        assert 'VA' == data['postalInfo'][0]['addr']['sp']
        assert '20166-6503' == data['postalInfo'][0]['addr']['pc']
        assert 'US' == data['postalInfo'][0]['addr']['cc']
        assert '1234' == data['voice']['@x']
        assert '+1.7035555555' == data['voice']['_text']
        assert '+1.7035555556' == data['fax']
        assert 'jdoe@example.com' == data['email']
        assert 'ClientY' == data['clID']
        assert 'ClientX' == data['crID']
        assert '1999-04-03T22:00:00.0Z' == data['crDate']
        assert 'ClientX' == data['upID']
        assert '1999-12-03T09:00:00.0Z' == data['upDate']
        assert '2000-04-08T09:00:00.0Z' == data['trDate']
        assert '2fooBAR' == data['authInfo']['pw']
        assert '0' == data['disclose']['@flag']
        assert '' == data['disclose']['voice']
        assert '' == data['disclose']['email']
        assert 'ABC-12345' == response['epp']['response']['trID']['clTRID']
        assert '54322-XYZ' == response['epp']['response']['trID']['svTRID']
        assert contactxmlschema.validate(etree.fromstring(xml))
        assert responseinfocontactcommandxmlexpected == xml
