from eppy.doc import EppInfoCommand

from registrobrepp.common.authinfo import AuthInfo


class BrEppInfoDefRegCommand(EppInfoCommand):
    def __init__(self, roid: str, authinfo: AuthInfo):
        dct = {
            'epp': {
                'command': {
                    'info': {
                        'defReg:info': {
                            'roid': roid,
                            'authInfo': authinfo
                        }
                    }
                }
            }
        }
        extra_nsmap = {'defReg': 'http://nic.br/epp/defReg-1.0'}
        super(BrEppInfoDefRegCommand, self).__init__(dct=self.annotate(dct), extra_nsmap=extra_nsmap)
