from eppy.doc import EppInfoContactCommand

from registrobrepp.common.authinfo import AuthInfo


class BrEppInfoContactCommand(EppInfoContactCommand):
    def __init__(self, id: str, authinfo: AuthInfo):
        dct = {
            'epp': {
                'command': {
                    'info': {
                        'contact:info': {
                            'id': id,
                            'authInfo': authinfo
                        }
                    }
                }
            }
        }
        extra_nsmap = {'brorg': 'urn:ietf:params:xml:ns:brorg-1.0'}
        super(BrEppInfoContactCommand, self).__init__(dct=self.annotate(dct), extra_nsmap=extra_nsmap)
