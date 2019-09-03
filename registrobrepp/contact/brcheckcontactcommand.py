from eppy.doc import EppCheckContactCommand


class BrEppCheckContactCommand(EppCheckContactCommand):
    def __init__(self, ids: list):
        dct = {
            'epp': {
                'command': {
                    'check': {
                        'contact:check': {
                            'id': ids
                        }
                    }
                }
            }
        }
        extra_nsmap = {'brorg': 'urn:ietf:params:xml:ns:brorg-1.0'}
        super(BrEppCheckContactCommand, self).__init__(dct=self.annotate(dct), extra_nsmap=extra_nsmap)
