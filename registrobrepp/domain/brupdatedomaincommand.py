from eppy.doc import EppUpdateDomainCommand

from registrobrepp.domain.adddomain import AddDomain
from registrobrepp.domain.chgdomain import ChgDomain
from registrobrepp.domain.remdomain import RemDomain


class BrEppUpdateDomainCommand(EppUpdateDomainCommand):
    def __init__(self, name: str, add: AddDomain = None, rem: RemDomain = None, chg: ChgDomain = None):
        dct = {
            'epp': {
                'command': {
                    'update': {
                        'domain:update': {
                            'name': name,
                            'add': add,
                            'rem': rem,
                            'chg': chg
                        }
                    }
                }
            }
        }
        extra_nsmap = {'brdomain': 'urn:ietf:params:xml:ns:brdomain-1.0'}
        super(BrEppUpdateDomainCommand, self).__init__(dct=self.annotate(dct), extra_nsmap=extra_nsmap)
