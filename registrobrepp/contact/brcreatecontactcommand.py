from eppy.doc import EppCreateContactCommand

from registrobrepp.common.authinfo import AuthInfo
from registrobrepp.contact.disclose import Disclose
from registrobrepp.contact.phone import Phone
from registrobrepp.contact.postalinfo import PostalInfo


class BrEppCreateContactCommand(EppCreateContactCommand):
    def __init__(self, id, postalinfo1: PostalInfo, email: str, authinfo: AuthInfo, postalinfo2: PostalInfo = None,
                 voice: Phone = None, fax: Phone = None, disclose: Disclose = None):
        postalInfo = [postalinfo1]
        if postalinfo2:
            postalInfo.append(postalinfo2)
        dct = {
            'epp': {
                'command': {
                    'create': {
                        'contact:create': {
                            'id': id,
                            'postalInfo': postalInfo,
                            'voice': voice,
                            'fax': fax,
                            'email': email,
                            'authInfo': authinfo,
                            'disclose': disclose
                        }
                    }
                }
            }
        }
        extra_nsmap = {
            'lacniccontact': 'urn:ietf:params:xml:ns:lacniccontact-1.0',
            'brorg': 'urn:ietf:params:xml:ns:brorg-1.0',
            'lacnicorg': 'urn:ietf:params:xml:ns:lacnicorg-1.0'
        }
        super(BrEppCreateContactCommand, self).__init__(dct=self.annotate(dct), extra_nsmap=extra_nsmap)
