from eppy.doc import EppTransferContactCommand

from registrobrepp.common.authinfo import AuthInfo


class BrEppTransferContactCommand(EppTransferContactCommand):
    def __init__(self, op: str, id: str, authinfo: AuthInfo):
        super(BrEppTransferContactCommand, self).__init__(op=op)
        self.id = id
        self.authInfo = authinfo
