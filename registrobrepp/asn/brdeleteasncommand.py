from eppy.doc import EppCommand


class BrEppDeleteAsnCommand(EppCommand):
    _path = ('epp', 'command', 'delete', 'asn:delete')

    def __init__(self, number: int):
        dct = {
            'epp': {
                'command': {
                    'delete': {
                        'asn:delete': {
                            'number': number
                        }
                    }
                }
            }
        }
        extra_nsmap = {'asn': 'urn:ietf:params:xml:ns:asn-1.0'}
        super(BrEppDeleteAsnCommand, self).__init__(dct=self.annotate(dct), extra_nsmap=extra_nsmap)
