from eppy.doc import EppCheckContactCommand


class BrEppCheckContactCommand(EppCheckContactCommand):
    def __init__(self, ids: list):
        super(BrEppCheckContactCommand, self).__init__()

        self.id = ids
