import datetime

from eppy.doc import EppRenewCommand

from registrobrepp.common.periodtype import PeriodType


class BrEppRenewDefRegCommand(EppRenewCommand):
    def __init__(self, roid: str, curexpdate: datetime, period: int, periodtype: PeriodType = PeriodType.YEAR):
        dct = {
            'epp': {
                'command': {
                    'renew': {
                        'defReg:renew': {
                            'roid': roid,
                            'curExpDate': curexpdate.strftime('%Y-%m-%d'),
                            'period': {'@unit': periodtype.value, '_text': period}
                        }
                    }
                }
            }
        }
        extra_nsmap = {'defReg': 'http://nic.br/epp/defReg-1.0'}
        super(BrEppRenewDefRegCommand, self).__init__(dct=self.annotate(dct), extra_nsmap=extra_nsmap)
