from eppy.doc import EppCreateDomainCommand
from eppy.xmldict import XmlDictObject

from registrobrepp.common.authinfo import AuthInfo
from registrobrepp.common.periodtype import PeriodType


class BrEppCreateDomainCommand(EppCreateDomainCommand):
    def __init__(self, name,  ns: XmlDictObject, authinfo: AuthInfo = None, period: int = 0, periodtype: PeriodType = PeriodType.YEAR,
                 registrant: str = None, contacts: list = None):
        pd = None
        if period > 0:
            pd = {'@unit': periodtype.value, '_text': period}
        dct = {
            'epp': {
                'command': {
                    'create': {
                        'domain:create': {
                            'name': name,
                            'period': pd,
                            'ns': ns,
                            'registrant': registrant,
                            'contact': contacts,
                            'authInfo': authinfo
                        }
                    }
                }
            }
        }
        extra_nsmap = {'brdomain': 'urn:ietf:params:xml:ns:brdomain-1.0'}
        super(BrEppCreateDomainCommand, self).__init__(dct=self.annotate(dct), extra_nsmap=extra_nsmap)
