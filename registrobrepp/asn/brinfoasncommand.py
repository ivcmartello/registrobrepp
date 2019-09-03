from eppy.doc import EppCommand


class BrEppInfoAsnCommand(EppCommand):
    _path = ('epp', 'command', 'info', 'asn:info')

    def __init__(self, number: int):
        dct = {
            'epp': {
                'command': {
                    'info': {
                        'asn:info': {
                            'number': number
                        }
                    }
                }
            }
        }
        extra_nsmap = {'asn': 'urn:ietf:params:xml:ns:asn-1.0'}
        super(BrEppInfoAsnCommand, self).__init__(dct=self.annotate(dct), extra_nsmap=extra_nsmap)
