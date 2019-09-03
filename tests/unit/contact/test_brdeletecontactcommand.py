import pytest
from eppy.doc import EppResponse
from lxml import etree

from registrobrepp.contact.brdeletecontactcommand import BrEppDeleteContactCommand
from registrobrepp.contact.eppdeletebrorg import EppDeleteBrOrg


class TestBrDeleteContactCommand:

    @pytest.fixture
    def deletecontactcommand(self):
        command = BrEppDeleteContactCommand('ab-12345')
        command.add_clTRID('ABC-12345')
        return command

    def test_delete_contact_command(self, deletecontactcommand, contactxmlschema, deletecontactcommandxmlexpected):
        xml = deletecontactcommand.to_xml(force_prefix=True).decode()

        assert contactxmlschema.validate(etree.fromstring(xml))
        assert xml == deletecontactcommandxmlexpected

    def test_delete_contact_command_with_brorg_extension(self, deletecontactcommand, brorgxmlschema,
                                                         deletecontactcommandwithbrorgxmlexpected):
        deletebrorg = EppDeleteBrOrg('005.506.560/0001-36')
        deletebrorgxml = deletebrorg.to_xml(force_prefix=True).decode()
        deletecontactcommand.add_command_extension(deletebrorg)
        xml = deletecontactcommand.to_xml(force_prefix=True).decode()

        assert brorgxmlschema.validate(etree.fromstring(deletebrorgxml))
        assert xml == deletecontactcommandwithbrorgxmlexpected

    def test_delete_contact_response(self, contactxmlschema, responsedeletecontactcommandxmlexpected):
        response = EppResponse.from_xml(responsedeletecontactcommandxmlexpected)
        xml = response.to_xml(force_prefix=True).decode()

        assert response['epp']['response']['trID']['clTRID'] == 'ABC-12345'
        assert response['epp']['response']['trID']['svTRID'] == '54321-XYZ'
        assert contactxmlschema.validate(etree.fromstring(xml))
        assert xml == responsedeletecontactcommandxmlexpected
