from eppy.doc import EppDoc

from registrobrepp.contact.addlacniccontact import AddLacnicContact
from registrobrepp.contact.chglacniccontact import ChgLacnicContact
from registrobrepp.contact.remlacniccontact import RemLacnicContact


class EppUpdateLacnicContact(EppDoc):
    _path = ('lacniccontact:update', )

    def __init__(self, add: AddLacnicContact = None, rem: RemLacnicContact = None, chg: ChgLacnicContact = None):
        dct = {
            'lacniccontact:update': {
                'add': add,
                'rem': rem,
                'chg': chg
            },
        }

        super(EppUpdateLacnicContact, self).__init__(dct, extra_nsmap={'lacniccontact': 'urn:ietf:params:xml:ns:lacniccontact-1.0'})
