from eppy.doc import EppCheckCommand


class BrEppCheckDefRegCommand(EppCheckCommand):
    def __init__(self, names: list):
        dct = {
            'epp': {
                'command': {
                    'check': {
                        'defReg:check': {
                            'name': names
                        }
                    }
                }
            }
        }
        extra_nsmap = {'defReg': 'http://nic.br/epp/defReg-1.0'}
        super(BrEppCheckDefRegCommand, self).__init__(dct=self.annotate(dct), extra_nsmap=extra_nsmap)
