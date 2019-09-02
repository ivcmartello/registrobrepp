from eppy.doc import EppInfoContactCommand

from registrobrepp.common.authinfo import AuthInfo


class BrEppInfoContactCommand(EppInfoContactCommand):
    def __init__(self, id: str, authinfo: AuthInfo):
        super(BrEppInfoContactCommand, self).__init__(extra_nsmap={'brorg': 'urn:ietf:params:xml:ns:brorg-1.0'})

        self.id = id
        self.authInfo = authinfo
