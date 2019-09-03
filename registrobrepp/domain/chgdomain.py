from eppy.xmldict import XmlDictObject

from registrobrepp.common.authinfo import AuthInfo


class ChgDomain(XmlDictObject):
    def __init__(self, registrant: str, authinfo: AuthInfo):
        dct = {
            'registrant': registrant,
            'authInfo': authinfo
        }
        super(ChgDomain, self).__init__(initdict=dct)
