from eppy.doc import EppCreateContactCommand

from registrobrepp.common.authinfo import AuthInfo
from registrobrepp.contact.disclose import Disclose
from registrobrepp.contact.phone import Phone
from registrobrepp.contact.postalinfo import PostalInfo


class BrEppCreateContactCommand(EppCreateContactCommand):
    def __init__(self, id, postalinfo1: PostalInfo, email: str, authinfo: AuthInfo, postalinfo2: PostalInfo = None,
                 voice: Phone = None, fax: Phone = None, disclose: Disclose = None):
        ex_nsmap = {
            'lacniccontact': 'urn:ietf:params:xml:ns:lacniccontact-1.0',
            'brorg': 'urn:ietf:params:xml:ns:brorg-1.0',
            'lacnicorg': 'urn:ietf:params:xml:ns:lacnicorg-1.0'
        }

        super(BrEppCreateContactCommand, self).__init__(extra_nsmap=ex_nsmap)

        self.id = id
        self.postalInfo = [postalinfo1]
        if postalinfo2:
            self.postalInfo.append(postalinfo2)
        self.voice = voice
        self.fax = fax
        self.email = email
        self.authInfo = authinfo
        self.disclose = disclose
