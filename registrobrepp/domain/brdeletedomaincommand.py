from eppy.doc import EppDeleteDomainCommand


class BrEppDeleteDomainCommand(EppDeleteDomainCommand):
    def __init__(self, name: str):
        super(BrEppDeleteDomainCommand, self).__init__()

        self.name = name