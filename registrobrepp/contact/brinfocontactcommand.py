from eppy.doc import EppInfoContactCommand

from registrobrepp.authinfo import AuthInfo


class BrEppInfoContactCommand(EppInfoContactCommand):
    def __init__(self, id: str, authinfo: AuthInfo):
        super(BrEppInfoContactCommand, self).__init__()

        self.id = id
        self.authInfo = authinfo
