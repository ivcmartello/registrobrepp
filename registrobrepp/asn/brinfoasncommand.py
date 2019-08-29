from eppy.doc import EppCommand


class BrEppInfoAsnCommand(EppCommand):
    _path = ('epp', 'command', 'info', 'asn:info')

    def __init__(self, number: int):
        ex_nsmap = {'asn': 'urn:ietf:params:xml:ns:asn-1.0'}
        super(BrEppInfoAsnCommand, self).__init__(extra_nsmap=ex_nsmap)

        self.number = number