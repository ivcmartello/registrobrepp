from eppy.doc import EppUpdateCommand

from registrobrepp.defreg.adddefreg import AddDefReg
from registrobrepp.defreg.chgdefreg import ChgDefReg
from registrobrepp.defreg.remdefreg import RemDefReg


class BrEppUpdateDefRegCommand(EppUpdateCommand):
    def __init__(self, roid: str, add: AddDefReg = None, rem: RemDefReg = None, chg: ChgDefReg = None):
        dct = {
            'epp': {
                'command': {
                    'update': {
                        'defReg:update': {
                            'roid': roid,
                            'add': add,
                            'rem': rem,
                            'chg': chg
                        }
                    }
                }
            }
        }
        extra_nsmap = {'defReg': 'http://nic.br/epp/defReg-1.0'}
        super(BrEppUpdateDefRegCommand, self).__init__(dct=self.annotate(dct), extra_nsmap=extra_nsmap)
