from eppy.doc import EppDeleteContactCommand


class BrEppDeleteContactCommand(EppDeleteContactCommand):
    def __init__(self, id: str):
        super(BrEppDeleteContactCommand, self).__init__(extra_nsmap={'brorg': 'urn:ietf:params:xml:ns:brorg-1.0'})

        self.id = id