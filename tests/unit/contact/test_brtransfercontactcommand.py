from eppy.doc import EppResponse
from lxml import etree

from registrobrepp.common.authinfo import AuthInfo
from registrobrepp.contact.brtransfercontactcommand import BrEppTransferContactCommand


class TestBrTransferContactCommand:

    def test_transfer_contact_query_command(self, contactxmlschema, transferquerycontactcommandxmlexpected):
        authinfo = AuthInfo('123')
        command = BrEppTransferContactCommand('query', 'ab-12345', authinfo)
        command.add_clTRID('ABC-12345')
        xml = command.to_xml(force_prefix=True).decode()

        assert contactxmlschema.validate(etree.fromstring(xml))
        assert xml == transferquerycontactcommandxmlexpected

    def test_transfer_contact_query_response(self, contactxmlschema, responsetransferquerycontactcommandxmlexpected):
        response = EppResponse.from_xml(responsetransferquerycontactcommandxmlexpected)
        xml = response.to_xml(force_prefix=True).decode()
        data = response['epp']['response']['resData']['contact:trnData']

        assert data.id == 'sh8013'
        assert data.trStatus == 'pending'
        assert data.reID == 'ClientX'
        assert data.reDate == '2000-06-06T22:00:00.0Z'
        assert data.acID == 'ClientY'
        assert data.acDate == '2000-06-11T22:00:00.0Z'
        assert response['epp']['response']['trID']['clTRID'] == 'ABC-12345'
        assert response['epp']['response']['trID']['svTRID'] == '54322-XYZ'
        assert contactxmlschema.validate(etree.fromstring(xml))
        assert xml == responsetransferquerycontactcommandxmlexpected

    def test_transfer_contact_request_command(self, contactxmlschema, transferrequestcontactcommandxmlexpected):
        authinfo = AuthInfo('123')
        command = BrEppTransferContactCommand('request', 'ab-12345', authinfo)
        command.add_clTRID('ABC-12345')
        xml = command.to_xml(force_prefix=True).decode()

        assert contactxmlschema.validate(etree.fromstring(xml))
        assert xml == transferrequestcontactcommandxmlexpected

    def test_transfer_contact_request_response(self, contactxmlschema, responsetransferrequestcontactcommandxmlexpected):
        response = EppResponse.from_xml(responsetransferrequestcontactcommandxmlexpected)
        xml = response.to_xml(force_prefix=True).decode()
        data = response['epp']['response']['resData']['contact:trnData']

        assert data.id == 'sh8013'
        assert data.trStatus == 'pending'
        assert data.reID == 'ClientX'
        assert data.reDate == '2000-06-08T22:00:00.0Z'
        assert data.acID == 'ClientY'
        assert data.acDate == '2000-06-13T22:00:00.0Z'
        assert response['epp']['response']['trID']['clTRID'] == 'ABC-12345'
        assert response['epp']['response']['trID']['svTRID'] == '54322-XYZ'
        assert contactxmlschema.validate(etree.fromstring(xml))
        assert responsetransferrequestcontactcommandxmlexpected == xml
