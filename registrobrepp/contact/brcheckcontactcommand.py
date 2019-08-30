from eppy.doc import EppCheckContactCommand


class BrEppCheckContactCommand(EppCheckContactCommand):
    def __init__(self, ids: list):
        super(BrEppCheckContactCommand, self).__init__(extra_nsmap={'brorg': 'urn:ietf:params:xml:ns:brorg-1.0'})

        self.id = ids
