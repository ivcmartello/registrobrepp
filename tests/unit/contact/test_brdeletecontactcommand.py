from eppy.doc import EppResponse
from lxml import etree

from registrobrepp.contact.brdeletecontactcommand import BrEppDeleteContactCommand


class TestBrDeleteContactCommand:

    def test_delete_contact_command(self, contactxmlschema, deletecontactcommandxmlexpected):
        command = BrEppDeleteContactCommand('ab-12345')
        command.add_clTRID('ABC-12345')
        xml = command.to_xml(force_prefix=False).decode()

        assert contactxmlschema.validate(etree.fromstring(xml))
        assert deletecontactcommandxmlexpected == xml

    def test_delete_contact_response(self, contactxmlschema, responsedeletecontactcommandxmlexpected):
        response = EppResponse.from_xml(responsedeletecontactcommandxmlexpected)
        xml = response.to_xml(force_prefix=False).decode()

        assert 'ABC-12345' == response['epp']['response']['trID']['clTRID']
        assert '54321-XYZ' == response['epp']['response']['trID']['svTRID']
        assert contactxmlschema.validate(etree.fromstring(xml))
        assert responsedeletecontactcommandxmlexpected == xml