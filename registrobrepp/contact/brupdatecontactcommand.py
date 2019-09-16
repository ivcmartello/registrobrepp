from eppy.doc import EppUpdateContactCommand

from registrobrepp.contact.chgcontact import ChgContact


class BrEppUpdateContactCommand(EppUpdateContactCommand):
    def __init__(self, id: str, status_add: list = None, status_rem: list = None, chg: ChgContact = None):

        if not status_add and not status_rem and not chg:
            raise ValueError('At least one <contact:add>, <contact:rem>, or <contact:chg> element MUST be provided')

        add = None
        rem = None

        if status_add:
            add = {'status': status_add}

        if status_rem:
            rem = {'status': status_rem}

        dct = {
            'epp': {
                'command': {
                    'update': {
                        'contact:update': {
                            'id': id,
                            'add': add,
                            'rem': rem,
                            'chg': chg
                        }
                    }
                }
            }
        }
        extra_nsmap = {
            'lacniccontact': 'urn:ietf:params:xml:ns:lacniccontact-1.0',
            'brorg': 'urn:ietf:params:xml:ns:brorg-1.0',
            'lacnicorg': 'urn:ietf:params:xml:ns:lacnicorg-1.0'
        }
        super(BrEppUpdateContactCommand, self).__init__(dct=self.annotate(dct), extra_nsmap=extra_nsmap)
