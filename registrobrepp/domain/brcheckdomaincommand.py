from eppy.doc import EppCheckDomainCommand


class BrEppCheckDomainCommand(EppCheckDomainCommand):
    def __init__(self, names: list):
        ex_nsmap = {'brdomain': 'urn:ietf:params:xml:ns:brdomain-1.0'}
        super(BrEppCheckDomainCommand, self).__init__(extra_nsmap=ex_nsmap)

        self.name = names