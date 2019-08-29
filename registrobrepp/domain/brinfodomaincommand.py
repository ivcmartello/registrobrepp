from eppy.doc import EppInfoDomainCommand

from registrobrepp.common.authinfo import AuthInfo
from registrobrepp.domain.infohost import InfoHost


class BrEppInfoDomainCommand(EppInfoDomainCommand):
    def __init__(self, name: str, authinfo: AuthInfo, hosts: InfoHost = InfoHost.ALL):
        ex_nsmap = {'brdomain': 'urn:ietf:params:xml:ns:brdomain-1.0'}
        super(BrEppInfoDomainCommand, self).__init__(extra_nsmap=ex_nsmap)

        self.name = {'@hosts': hosts.value, '_text': name}
        self.authInfo = authinfo