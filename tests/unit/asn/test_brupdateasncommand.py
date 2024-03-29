import datetime

import pytest
from eppy.doc import EppResponse
from lxml import etree

from registrobrepp.asn.addasn import AddAsn
from registrobrepp.asn.brupdateasncommand import BrEppUpdateAsnCommand
from registrobrepp.asn.chgasn import ChgAsn
from registrobrepp.asn.contactasn import ContactAsn
from registrobrepp.asn.remasn import RemAsn


class TestBrUpdateAsnCommand:

    def test_update_asn_command(self, asnxmlschema, updateasncommandxmlexpected):
        number = 64500
        contactsadd = [ContactAsn.build('fan', routing=True)]
        asIn = ['from AS2 10 accept AS1 A2']
        add = AddAsn(contactsadd, asIn)
        contactsrem = [ContactAsn.build('hkk')]
        asOut = ['to AS2 announce AS3 AS4']
        rem = RemAsn(contactsrem, asOut)
        chg = ChgAsn('BR-ABCD-LACNIC')
        creationdate = datetime.datetime(2011, 1, 27, 00, 00, 00)

        command = BrEppUpdateAsnCommand(number, creationdate, add, rem, chg)
        command.add_clTRID('ABC-12345')
        xml = command.to_xml(force_prefix=True).decode()

        assert asnxmlschema.validate(etree.fromstring(xml))
        assert xml == updateasncommandxmlexpected

    def test_update_asn_command_without_add_rem_chg(self):
        number = 64500
        creationdate = datetime.datetime(2011, 1, 27, 00, 00, 00)
        with pytest.raises(ValueError, match='At least one <asn:add>, <asn:rem>, or <asn:chg> element MUST be provided'):
            BrEppUpdateAsnCommand(number, creationdate)

    def test_update_asn_response(self, asnxmlschema, responseupdateasncommandxmlexpected):
        response = EppResponse.from_xml(responseupdateasncommandxmlexpected,
                                        extra_nsmap={'asn': 'urn:ietf:params:xml:ns:asn-1.0'})
        xml = response.to_xml(force_prefix=True).decode()

        assert response['epp']['response']['trID']['clTRID'] == 'ABC-12345'
        assert response['epp']['response']['trID']['svTRID'] == '54321-XYZ'
        assert asnxmlschema.validate(etree.fromstring(xml))
