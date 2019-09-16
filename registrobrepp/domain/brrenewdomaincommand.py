import datetime

from eppy.doc import EppRenewDomainCommand

from registrobrepp.common.periodtype import PeriodType


class BrEppRenewDomainCommand(EppRenewDomainCommand):
    def __init__(self, name: str, curexpdate: datetime, period: int = 0, periodunit: PeriodType = PeriodType.YEAR):
        pd = None
        if period > 0:
            pd = {'@unit': periodunit.value, '_text': period}
        dct = {
            'epp': {
                'command': {
                    'renew': {
                        'domain:renew': {
                            'name': name,
                            'curExpDate': curexpdate.strftime('%Y-%m-%d'),
                            'period': pd
                        }
                    }
                }
            }
        }
        super(BrEppRenewDomainCommand, self).__init__(dct=self.annotate(dct))
