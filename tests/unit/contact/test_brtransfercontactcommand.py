from eppy.doc import EppResponse
from lxml import etree

from registrobrepp.common.authinfo import AuthInfo
from registrobrepp.contact.brtransfercontactcommand import BrEppTransferContactCommand


class TestBrTransferContactCommand:

    def test_transfer_contact_query_command(self, contactxmlschema, transferquerycontactcommandxmlexpected):
        authinfo = AuthInfo('123')
        command = BrEppTransferContactCommand('query', 'ab-12345', authinfo)
        command.add_clTRID('ABC-12345')
        xml = command.to_xml(force_prefix=False).decode()

        assert contactxmlschema.validate(etree.fromstring(xml))
        assert transferquerycontactcommandxmlexpected == xml

    def test_transfer_contact_query_response(self, contactxmlschema, responsetransferquerycontactcommandxmlexpected):
        response = EppResponse.from_xml(responsetransferquerycontactcommandxmlexpected)
        xml = response.to_xml(force_prefix=False).decode()
        data = response['epp']['response']['resData']['contact:trnData']

        assert 'sh8013' == data['id']
        assert 'pending' == data['trStatus']
        assert 'ClientX' == data['reID']
        assert '2000-06-06T22:00:00.0Z' == data['reDate']
        assert 'ClientY' == data['acID']
        assert '2000-06-11T22:00:00.0Z' == data['acDate']
        assert 'ABC-12345' == response['epp']['response']['trID']['clTRID']
        assert '54322-XYZ' == response['epp']['response']['trID']['svTRID']
        assert contactxmlschema.validate(etree.fromstring(xml))
        assert responsetransferquerycontactcommandxmlexpected == xml

    def test_transfer_contact_request_command(self, contactxmlschema, transferrequestcontactcommandxmlexpected):
        authinfo = AuthInfo('123')
        command = BrEppTransferContactCommand('request', 'ab-12345', authinfo)
        command.add_clTRID('ABC-12345')
        xml = command.to_xml(force_prefix=False).decode()

        assert contactxmlschema.validate(etree.fromstring(xml))
        assert transferrequestcontactcommandxmlexpected == xml

    def test_transfer_contact_request_response(self, contactxmlschema, responsetransferrequestcontactcommandxmlexpected):
        response = EppResponse.from_xml(responsetransferrequestcontactcommandxmlexpected)
        xml = response.to_xml(force_prefix=False).decode()
        data = response['epp']['response']['resData']['contact:trnData']

        assert 'sh8013' == data['id']
        assert 'pending' == data['trStatus']
        assert 'ClientX' == data['reID']
        assert '2000-06-08T22:00:00.0Z' == data['reDate']
        assert 'ClientY' == data['acID']
        assert '2000-06-13T22:00:00.0Z' == data['acDate']
        assert 'ABC-12345' == response['epp']['response']['trID']['clTRID']
        assert '54322-XYZ' == response['epp']['response']['trID']['svTRID']
        assert contactxmlschema.validate(etree.fromstring(xml))
        assert responsetransferrequestcontactcommandxmlexpected == xml
