import datetime

from eppy.doc import EppResponse
from lxml import etree

from registrobrepp.asn.brrenewasncommand import BrEppRenewAsnCommand


class TestBrRenewAsnCommand:

    def test_renew_asn_command(self, asnxmlschema, renewasncommandxmlexpected):
        number = 64500
        curexpdate = datetime.datetime(2008, 4, 3, 00, 00, 00)
        command = BrEppRenewAsnCommand(number, curexpdate, period=3)
        command.add_clTRID('ABC-12345')
        xml = command.to_xml(force_prefix=True).decode()

        assert asnxmlschema.validate(etree.fromstring(xml))
        assert xml == renewasncommandxmlexpected

    def test_renew_asn_response(self, asnxmlschema, responserenewasncommandxmlexpected):
        response = EppResponse.from_xml(responserenewasncommandxmlexpected,
                                        extra_nsmap={'asn': 'urn:ietf:params:xml:ns:asn-1.0'})
        xml = response.to_xml(force_prefix=True).decode()
        data = response['epp']['response']['resData']['asn:renData']

        assert data.number == '64500'
        assert data.exDate == '2011-04-03T00:00:00.0Z'
        assert asnxmlschema.validate(etree.fromstring(xml))
