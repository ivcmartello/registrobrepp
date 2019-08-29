from eppy.doc import EppCommand


class BrEppCheckAsnCommand(EppCommand):
    _path = ('epp', 'command', 'check', 'asn:check')

    def __init__(self, numbers: list):
        ex_nsmap = {'asn': 'urn:ietf:params:xml:ns:asn-1.0'}
        super(BrEppCheckAsnCommand, self).__init__(extra_nsmap=ex_nsmap)

        self.number = numbers