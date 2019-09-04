import datetime

from eppy.doc import EppRenewCommand

from registrobrepp.common.periodtype import PeriodType


class BrEppRenewIpNetworkCommand(EppRenewCommand):
    def __init__(self, roid: str, curexpdate: datetime, period: int, periodtype: PeriodType = PeriodType.YEAR):
        dct = {
            'epp': {
                'command': {
                    'renew': {
                        'ipnetwork:renew': {
                            'roid': roid,
                            'curExpDate': curexpdate.strftime('%Y-%m-%dT%H:%M:%S.0Z'),
                            'period': {'@unit': periodtype.value, '_text': period}
                        }
                    }
                }
            }
        }
        extra_nsmap = {'ipnetwork': 'urn:ietf:params:xml:ns:ipnetwork-1.0'}
        super(BrEppRenewIpNetworkCommand, self).__init__(dct=self.annotate(dct), extra_nsmap=extra_nsmap)
