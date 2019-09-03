from eppy.doc import EppDeleteContactCommand


class BrEppDeleteContactCommand(EppDeleteContactCommand):
    def __init__(self, id: str):
        dct = {
            'epp': {
                'command': {
                    'delete': {
                        'contact:delete': {
                            'id': id
                        }
                    }
                }
            }
        }
        extra_nsmap = {'brorg': 'urn:ietf:params:xml:ns:brorg-1.0'}
        super(BrEppDeleteContactCommand, self).__init__(dct=self.annotate(dct), extra_nsmap=extra_nsmap)
