import pytest
from eppy.doc import EppResponse
from lxml import etree

from registrobrepp.asn.brcreateasncommand import BrEppCreateAsnCommand
from registrobrepp.asn.contactasn import ContactAsn


class TestBrCreateAsnCommand:

    @pytest.fixture
    def createasncommand(self):
        number = 12345
        organization = 'BR-ABCD-LACNIC'
        contacts = [ContactAsn.build('fan', routing=True), ContactAsn.build('hkk')]
        asIn = ['from AS2 10 accept AS1 A2']
        asOut = ['to AS2 announce AS3 AS4']
        command = BrEppCreateAsnCommand(number, organization, contacts, asIn, asOut)
        command.add_clTRID('ABC-12345')
        return command

    def test_create_asn_command(self, createasncommand, asnxmlschema, createasncommandxmlexpected):
        xml = createasncommand.to_xml(force_prefix=False).decode()

        assert asnxmlschema.validate(etree.fromstring(xml))
        assert createasncommandxmlexpected == xml

    def test_create_asn_response(self, asnxmlschema, responseasncommandxmlexpected):
        response = EppResponse.from_xml(responseasncommandxmlexpected,
                                        extra_nsmap={'asn': 'urn:ietf:params:xml:ns:asn-1.0'})
        xml = response.to_xml(force_prefix=False).decode()
        data = response['epp']['response']['resData']['asn:creData']

        assert '64500' == data['number']
        assert '64500-REP' == data['roid']
        assert '1999-04-03T22:00:00.0Z' == data['crDate']
        assert 'ABC-12345' == response['epp']['response']['trID']['clTRID']
        assert '54321-XYZ' == response['epp']['response']['trID']['svTRID']
        assert asnxmlschema.validate(etree.fromstring(xml))
