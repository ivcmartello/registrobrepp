from eppy.doc import EppCommand


class BrEppTransferAsnCommand(EppCommand):
    _path = ('epp', 'command', 'transfer', 'asn:transfer')

    def __init__(self, op: str, number: int):
        ex_nsmap = {'asn': 'urn:ietf:params:xml:ns:asn-1.0'}
        super(BrEppTransferAsnCommand, self).__init__(extra_nsmap=ex_nsmap)

        self['epp']['command']['transfer']['@op'] = op
        self.number = number