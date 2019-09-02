from eppy.doc import EppResponse
from lxml import etree

from registrobrepp.asn.brinfoasncommand import BrEppInfoAsnCommand


class TestBrInfoAsnCommand:

    def test_info_asn_command(self, asnxmlschema, infoasncommandxmlexpected):
        number = 64500
        command = BrEppInfoAsnCommand(number)
        command.add_clTRID('ABC-12345')
        xml = command.to_xml(force_prefix=True).decode()

        assert asnxmlschema.validate(etree.fromstring(xml))
        assert infoasncommandxmlexpected == xml

    def test_info_asn_response(self, asnxmlschema, responseinfoasncommandxmlexpected):
        response = EppResponse.from_xml(responseinfoasncommandxmlexpected,
                                        extra_nsmap={'asn': 'urn:ietf:params:xml:ns:asn-1.0'})
        xml = response.to_xml(force_prefix=True).decode()
        data = response['epp']['response']['resData']['asn:infData']

        assert '64500' == data.number
        assert '64500-REP' == data.roid
        assert 'BR-ABCD-LACNIC' == data.organization
        assert 'routing' == data.contact[0]['@type']
        assert 'fan' == data.contact[0]['_text']
        assert 'security' == data.contact[1]['@type']
        assert 'hkk' == data.contact[1]['_text']
        assert 'ClientY' == data.clID
        assert 'ClientX' == data.crID
        assert '1999-04-03T22:00:00.0Z' == data.crDate
        assert 'ClientX' == data.upID
        assert '2005-12-03T09:00:00.0Z' == data.upDate
        assert '2004-04-08T09:00:00.0Z' == data.trDate
        assert 'from AS2 10 accept AS1 A2' == data.asIn[0]
        assert 'from AS3 10 accept AS1 A2' == data.asIn[1]
        assert 'to AS2 announce AS3 AS4' == data.asOut[0]
        assert 'to AS5 announce AS3 AS4' == data.asOut[1]
        assert 'ABC-12345' == response['epp']['response']['trID']['clTRID']
        assert '54322-XYZ' == response['epp']['response']['trID']['svTRID']
        assert asnxmlschema.validate(etree.fromstring(xml))
