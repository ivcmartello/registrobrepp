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
        assert xml == infoasncommandxmlexpected

    def test_info_asn_response(self, asnxmlschema, responseinfoasncommandxmlexpected):
        response = EppResponse.from_xml(responseinfoasncommandxmlexpected,
                                        extra_nsmap={'asn': 'urn:ietf:params:xml:ns:asn-1.0'})
        xml = response.to_xml(force_prefix=True).decode()
        data = response['epp']['response']['resData']['asn:infData']

        assert data.number == '64500'
        assert data.roid == '64500-REP'
        assert data.organization == 'BR-ABCD-LACNIC'
        assert data.contact[0]['@type'] == 'routing'
        assert data.contact[0]['_text'] == 'fan'
        assert data.contact[1]['@type'] == 'security'
        assert data.contact[1]['_text'] == 'hkk'
        assert data.clID == 'ClientY'
        assert data.crID == 'ClientX'
        assert data.crDate == '1999-04-03T22:00:00.0Z'
        assert data.upID == 'ClientX'
        assert data.upDate == '2005-12-03T09:00:00.0Z'
        assert data.trDate == '2004-04-08T09:00:00.0Z'
        assert data.asIn[0] == 'from AS2 10 accept AS1 A2'
        assert data.asIn[1] == 'from AS3 10 accept AS1 A2'
        assert data.asOut[0] == 'to AS2 announce AS3 AS4'
        assert data.asOut[1] == 'to AS5 announce AS3 AS4'
        assert response['epp']['response']['trID']['clTRID'] == 'ABC-12345'
        assert response['epp']['response']['trID']['svTRID'] == '54322-XYZ'
        assert asnxmlschema.validate(etree.fromstring(xml))
