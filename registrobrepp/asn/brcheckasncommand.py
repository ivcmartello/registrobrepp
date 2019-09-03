from eppy.doc import EppCommand


class BrEppCheckAsnCommand(EppCommand):
    _path = ('epp', 'command', 'check', 'asn:check')

    def __init__(self, numbers: list):
        dct = {
            'epp': {
                'command': {
                    'check': {
                        'asn:check': {
                            'number': numbers
                        }
                    }
                }
            }
        }
        extra_nsmap = {'asn': 'urn:ietf:params:xml:ns:asn-1.0'}
        super(BrEppCheckAsnCommand, self).__init__(dct=self.annotate(dct), extra_nsmap=extra_nsmap)
