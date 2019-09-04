import datetime

from eppy.doc import EppCreateCommand

from registrobrepp.common.authinfo import AuthInfo
from registrobrepp.defreg.namedefreg import NameDefReg


class BrEppCreateDefRegCommand(EppCreateCommand):
    def __init__(self, name: NameDefReg, registrant: str, tm: str, tmcountry: str, tmdate: datetime, admincontact: str,
                 authinfo: AuthInfo):
        dct = {
            'epp': {
                'command': {
                    'create': {
                        'defReg:create': {
                            'name': name,
                            'registrant': registrant,
                            'tm': tm,
                            'tmCountry': tmcountry,
                            'tmDate': tmdate.strftime('%Y-%m-%d'),
                            'adminContact': admincontact,
                            'authInfo': authinfo
                        }
                    }
                }
            }
        }
        extra_nsmap = {'defReg': 'http://nic.br/epp/defReg-1.0'}
        super(BrEppCreateDefRegCommand, self).__init__(dct=self.annotate(dct), extra_nsmap=extra_nsmap)
