from eppy.doc import EppUpdateContactCommand

from registrobrepp.contact.chgcontact import ChgContact


class BrEppUpdateContactCommand(EppUpdateContactCommand):
    def __init__(self, id: str, status_add: list = None, status_rem: list = None, chg: ChgContact = None):
        super(BrEppUpdateContactCommand, self).__init__(extra_nsmap={'lacniccontact': 'urn:ietf:params:xml:ns:lacniccontact-1.0'})

        self.id = id
        if status_add:
            self.add = {'status': status_add}
        if status_rem:
            self.rem = {'status': status_rem}
        self.chg = chg
