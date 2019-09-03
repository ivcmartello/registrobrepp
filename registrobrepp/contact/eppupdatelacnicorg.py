from eppy.doc import EppDoc

from registrobrepp.contact.addlacnicorg import AddLacnicOrg
from registrobrepp.contact.chglacnicorg import ChgLacnicOrg
from registrobrepp.contact.remlacnicorg import RemLacnicOrg


class EppUpdateLacnicOrg(EppDoc):
    _path = ('lacnicorg:update', )

    def __init__(self, password: str, add: AddLacnicOrg = None, rem: RemLacnicOrg = None, chg: ChgLacnicOrg = None):
        dct = {
            'lacnicorg:update': {
                'add': add,
                'rem': rem,
                'chg': chg,
                'password': password
            }
        }
        extra_nsmap = {'lacnicorg': 'urn:ietf:params:xml:ns:lacnicorg-1.0'}
        super(EppUpdateLacnicOrg, self).__init__(dct=self.annotate(dct), extra_nsmap=extra_nsmap)
