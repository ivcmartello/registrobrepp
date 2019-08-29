from eppy.doc import EppTransferDomainCommand

from registrobrepp.authinfo import AuthInfo


class BrEppTransferDomainCommand(EppTransferDomainCommand):
    def __init__(self, op: str, name: str, authinfo: AuthInfo, period: int = 0, periodunit: str = 'y'):
        super(BrEppTransferDomainCommand, self).__init__(op)

        self.name = name
        if period > 0:
            self.period = {'@unit': periodunit, '_text': period}
        self.authInfo = authinfo