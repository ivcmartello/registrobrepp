from eppy.doc import EppCommand


class BrEppTransferAsnCommand(EppCommand):
    _path = ('epp', 'command', 'transfer', 'asn:transfer')

    def __init__(self, op: str, number: int):
        super(BrEppTransferAsnCommand, self).__init__(extra_nsmap={'asn': 'urn:ietf:params:xml:ns:asn-1.0'})

        self['epp']['command']['transfer']['@op'] = op
        self.number = number