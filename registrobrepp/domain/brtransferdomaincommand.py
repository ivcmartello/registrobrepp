from eppy.doc import EppTransferDomainCommand

from registrobrepp.common.authinfo import AuthInfo
from registrobrepp.common.periodtype import PeriodType


class BrEppTransferDomainCommand(EppTransferDomainCommand):
    def __init__(self, op: str, name: str, authinfo: AuthInfo, period: int = 0, periodunit: PeriodType = PeriodType.YEAR):
        super(BrEppTransferDomainCommand, self).__init__(op)
        self.name = name
        if period > 0:
            self.period = {'@unit': periodunit.value, '_text': period}
        self.authInfo = authinfo