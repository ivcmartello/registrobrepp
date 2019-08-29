from eppy.doc import EppDeleteContactCommand


class BrEppDeleteContactCommand(EppDeleteContactCommand):
    def __init__(self, id: str):
        super(BrEppDeleteContactCommand, self).__init__()

        self.id = id