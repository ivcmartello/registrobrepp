from eppy.doc import EppCommand


class BrEppTransferAsnCommand(EppCommand):
    _path = ('epp', 'command', 'transfer', 'asn:transfer')

    def __init__(self, op: str, number: int):
        dct = {
            'epp': {
                'command': {
                    'transfer': {
                        '@op': op,
                        'asn:transfer': {
                            'number': number,
                        }
                    }
                }
            }
        }
        extra_nsmap = {'asn': 'urn:ietf:params:xml:ns:asn-1.0'}
        super(BrEppTransferAsnCommand, self).__init__(dct=self.annotate(dct), extra_nsmap=extra_nsmap)
