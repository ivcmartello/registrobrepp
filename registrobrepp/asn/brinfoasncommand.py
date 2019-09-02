from eppy.doc import EppCommand


class BrEppInfoAsnCommand(EppCommand):
    _path = ('epp', 'command', 'info', 'asn:info')

    def __init__(self, number: int):
        super(BrEppInfoAsnCommand, self).__init__(extra_nsmap={'asn': 'urn:ietf:params:xml:ns:asn-1.0'})

        self.number = number