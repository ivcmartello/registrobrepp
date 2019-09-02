from eppy.doc import EppCommand


class BrEppDeleteAsnCommand(EppCommand):
    _path = ('epp', 'command', 'delete', 'asn:delete')

    def __init__(self, number: int):
        super(BrEppDeleteAsnCommand, self).__init__(extra_nsmap={'asn': 'urn:ietf:params:xml:ns:asn-1.0'})

        self.number = number