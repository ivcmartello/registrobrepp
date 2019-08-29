import datetime

from eppy.doc import EppCommand


class BrEppRenewAsnCommand(EppCommand):
    _path = ('epp', 'command', 'renew', 'asn:renew')

    def __init__(self, number: int, curexpdate: datetime, period: int, periodtype: str = 'y'):
        ex_nsmap = {'asn': 'urn:ietf:params:xml:ns:asn-1.0'}
        super(BrEppRenewAsnCommand, self).__init__(extra_nsmap=ex_nsmap)

        self.number = number
        self.curExpDate = curexpdate.strftime('%Y-%m-%dT%H:%M:%S.0Z')
        self.period = {'@unit': periodtype, '_text': period}
