from eppy.doc import EppCommand


class BrEppCreateReserveAsnCommand(EppCommand):
    _path = ('epp', 'command', 'create', 'asnReserve:create')

    def __init__(self, startAsn: int, endAsn: int, organization: str, comment: str = None):
        dct = {
            'epp': {
                'command': {
                    'create': {
                        'asnReserve:create': {
                            'startASN': startAsn,
                            'endASN': endAsn,
                            'organization': organization,
                            'comment': comment
                        }
                    }
                }
            }
        }
        extra_nsmap = {'asnReserve': 'urn:ietf:params:xml:ns:asnReserve-1.0'}
        super(BrEppCreateReserveAsnCommand, self).__init__(dct=self.annotate(dct), extra_nsmap=extra_nsmap)
