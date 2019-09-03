from eppy.xmldict import XmlDictObject

from registrobrepp.common.authinfo import AuthInfo
from registrobrepp.contact.disclose import Disclose
from registrobrepp.contact.phone import Phone
from registrobrepp.contact.postalinfo import PostalInfo


class ChgContact(XmlDictObject):
    def __init__(self, postalinfo1: PostalInfo, email: str, authinfo: AuthInfo, postalinfo2: PostalInfo = None,
                 voice: Phone = None, fax: Phone = None, disclose: Disclose = None):
        postalinfo = [postalinfo1]
        if postalinfo2:
            postalinfo.append(postalinfo2)
        dct = {
            'postalInfo': postalinfo,
            'voice': voice,
            'fax': fax,
            'email': email,
            'authInfo': authinfo,
            'disclose': disclose
        }
        super(ChgContact, self).__init__(initdict=dct)
