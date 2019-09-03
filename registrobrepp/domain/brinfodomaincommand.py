from eppy.doc import EppInfoDomainCommand

from registrobrepp.common.authinfo import AuthInfo
from registrobrepp.domain.infohost import InfoHost


class BrEppInfoDomainCommand(EppInfoDomainCommand):
    def __init__(self, name: str, authinfo: AuthInfo, hosts: InfoHost = InfoHost.ALL):
        dct = {
            'epp': {
                'command': {
                    'info': {
                        'domain:info': {
                            'name': {'@hosts': hosts.value, '_text': name},
                            'authInfo': authinfo
                        }
                    }
                }
            }
        }
        extra_nsmap = {'brdomain': 'urn:ietf:params:xml:ns:brdomain-1.0'}
        super(BrEppInfoDomainCommand, self).__init__(dct=self.annotate(dct), extra_nsmap=extra_nsmap)
