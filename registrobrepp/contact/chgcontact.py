from eppy.xmldict import XmlDictObject

from registrobrepp.common.authinfo import AuthInfo
from registrobrepp.contact.disclose import Disclose
from registrobrepp.contact.phone import Phone
from registrobrepp.contact.postalinfo import PostalInfo


class ChgContact(XmlDictObject):
    def __init__(self, postalinfo1: PostalInfo, email: str, authinfo: AuthInfo, postalinfo2: PostalInfo = None,
                 voice: Phone = None, fax: Phone = None, disclose: Disclose = None):
        super(ChgContact, self).__init__()

        self.postalInfo = [postalinfo1]
        if postalinfo2:
            self.postalInfo.append(postalinfo2)
        self.voice = voice
        self.fax = fax
        self.email = email
        self.authInfo = authinfo
        self.disclose = disclose
