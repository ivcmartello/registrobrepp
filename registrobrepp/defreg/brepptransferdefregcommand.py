from eppy.doc import EppTransferCommand

from registrobrepp.common.authinfo import AuthInfo


class BrEppTransferDefRegCommand(EppTransferCommand):
    _path = ('epp', 'command', 'transfer', 'defReg:transfer')

    def __init__(self, op: str, roid: str, authinfo: AuthInfo):
        extra_nsmap = {'defReg': 'http://nic.br/epp/defReg-1.0'}
        super(BrEppTransferDefRegCommand, self).__init__(op=op, extra_nsmap=extra_nsmap)
        self.roid = roid
        self.authInfo = authinfo
