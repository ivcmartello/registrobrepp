from eppy.doc import EppDoc

from registrobrepp.contact.addbrorg import AddBrOrg
from registrobrepp.contact.chgbrorg import ChgBrOrg
from registrobrepp.contact.rembrorg import RemBrOrg


class EppUpdateBrOrg(EppDoc):
    _path = ('brorg:update',)

    def __init__(self, organization: str, add: AddBrOrg = None, rem: RemBrOrg = None, chg: ChgBrOrg = None):
        dct = {
            'brorg:update': {
                'organization': organization,
                'add': add,
                'rem': rem,
                'chg': chg
            }
        }
        extra_nsmap = {'brorg': 'urn:ietf:params:xml:ns:brorg-1.0'}
        super(EppUpdateBrOrg, self).__init__(dct=self.annotate(dct), extra_nsmap=extra_nsmap)