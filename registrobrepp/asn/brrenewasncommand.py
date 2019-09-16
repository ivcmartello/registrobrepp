import datetime

from eppy.doc import EppRenewCommand

from registrobrepp.common.periodtype import PeriodType


class BrEppRenewAsnCommand(EppRenewCommand):
    _path = ('epp', 'command', 'renew', 'asn:renew')

    def __init__(self, number: int, curexpdate: datetime, period: int, periodtype: PeriodType = PeriodType.YEAR):
        pd = None
        if period > 0:
            pd = {'@unit': periodtype.value, '_text': period}
        dct = {
            'epp': {
                'command': {
                    'renew': {
                        'asn:renew': {
                            'number': number,
                            'curExpDate': curexpdate.strftime('%Y-%m-%dT%H:%M:%S.0Z'),
                            'period': pd
                        }
                    }
                }
            }
        }
        extra_nsmap = {'asn': 'urn:ietf:params:xml:ns:asn-1.0'}
        super(BrEppRenewAsnCommand, self).__init__(dct=self.annotate(dct), extra_nsmap=extra_nsmap)
