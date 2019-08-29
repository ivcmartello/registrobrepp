from eppy.doc import EppCreateDomainCommand

from registrobrepp.authinfo import AuthInfo
from registrobrepp.domain.ns import Ns


class BrEppCreateDomainCommand(EppCreateDomainCommand):
    def __init__(self, name,  ns: Ns, authinfo: AuthInfo, period: int = 0, periodtype: str = 'y', registrant: str = None,
                 contacts: list = None):
        ex_nsmap = {'brdomain': 'urn:ietf:params:xml:ns:brdomain-1.0'}
        super(BrEppCreateDomainCommand, self).__init__(extra_nsmap=ex_nsmap)

        self.name = name
        if period > 0:
            self.period = {'@unit': periodtype, '_text': period}
        self.ns = ns
        self.registrant = registrant
        self.contact = contacts
        self.authInfo = authinfo