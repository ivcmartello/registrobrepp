import datetime

from eppy.doc import EppCommand

from registrobrepp.common.periodtype import PeriodType


class BrEppRenewAsnCommand(EppCommand):
    _path = ('epp', 'command', 'renew', 'asn:renew')

    def __init__(self, number: int, curexpdate: datetime, period: int, periodtype: PeriodType = PeriodType.YEAR):
        dct = {
            'epp': {
                'command': {
                    'renew': {
                        'asn:renew': {
                            'number': number,
                            'curExpDate': curexpdate.strftime('%Y-%m-%dT%H:%M:%S.0Z'),
                            'period': {'@unit': periodtype.value, '_text': period}
                        }
                    }
                }
            }
        }
        extra_nsmap = {'asn': 'urn:ietf:params:xml:ns:asn-1.0'}
        super(BrEppRenewAsnCommand, self).__init__(dct=self.annotate(dct), extra_nsmap=extra_nsmap)
