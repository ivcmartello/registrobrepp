from eppy.doc import EppTransferCommand


class BrEppTransferIpNetworkCommand(EppTransferCommand):
    _path = ('epp', 'command', 'transfer', 'ipnetwork:transfer')

    def __init__(self, op: str, roid: str):
        extra_nsmap = {'ipnetwork': 'urn:ietf:params:xml:ns:ipnetwork-1.0'}
        super(BrEppTransferIpNetworkCommand, self).__init__(op=op, extra_nsmap=extra_nsmap)
        self.roid = roid
