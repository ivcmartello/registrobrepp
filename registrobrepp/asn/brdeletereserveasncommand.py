from eppy.doc import EppDeleteCommand


class BrEppDeleteReserveAsnCommand(EppDeleteCommand):
    _path = ('epp', 'command', 'delete', 'asnReserve:delete')

    def __init__(self, id: int):
        dct = {
            'epp': {
                'command': {
                    'delete': {
                        'asnReserve:delete': {
                            'id': id
                        }
                    }
                }
            }
        }
        extra_nsmap = {'asnReserve': 'urn:ietf:params:xml:ns:asnReserve-1.0'}
        super(BrEppDeleteReserveAsnCommand, self).__init__(dct=self.annotate(dct), extra_nsmap=extra_nsmap)
