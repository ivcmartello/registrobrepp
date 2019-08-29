from eppy.xmldict import XmlDictObject

from registrobrepp.authinfo import AuthInfo


class ChgDomain(XmlDictObject):
    def __init__(self, registrant: str, authinfo: AuthInfo):
        super(ChgDomain, self).__init__()

        self.registrant = registrant
        self.authInfo = authinfo