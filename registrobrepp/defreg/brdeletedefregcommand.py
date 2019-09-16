from eppy.doc import EppDeleteCommand


class BrEppDeleteDefRegCommand(EppDeleteCommand):
    def __init__(self, roid: str):
        dct = {
            'epp': {
                'command': {
                    'delete': {
                        'defReg:delete': {
                            'roid': roid
                        }
                    }
                }
            }
        }
        extra_nsmap = {'defReg': 'http://nic.br/epp/defReg-1.0'}
        super(BrEppDeleteDefRegCommand, self).__init__(dct=self.annotate(dct), extra_nsmap=extra_nsmap)
