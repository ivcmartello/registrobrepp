import datetime

from eppy.doc import EppRenewDomainCommand


class BrEppRenewDomainCommand(EppRenewDomainCommand):
    def __init__(self, name: str, curexpdate: datetime.date, period: int = 0, periodunit: str = 'y'):
        super(BrEppRenewDomainCommand, self).__init__()

        self.name = name
        self.curExpDate = curexpdate
        if period > 0:
            self.period = {'@unit': periodunit, '_text': period}
