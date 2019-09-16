from eppy.doc import EppTransferCommand


class BrEppTransferAsnCommand(EppTransferCommand):
    _path = ('epp', 'command', 'transfer', 'asn:transfer')

    def __init__(self, op: str, number: int):
        extra_nsmap = {'asn': 'urn:ietf:params:xml:ns:asn-1.0'}
        super(BrEppTransferAsnCommand, self).__init__(op=op, extra_nsmap=extra_nsmap)
        self.number = number
