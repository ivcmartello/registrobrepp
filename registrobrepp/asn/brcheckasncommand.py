from eppy.doc import EppCommand


class BrEppCheckAsnCommand(EppCommand):
    _path = ('epp', 'command', 'check', 'asn:check')

    def __init__(self, numbers: list):
        super(BrEppCheckAsnCommand, self).__init__(
            extra_nsmap={
                'asn': 'urn:ietf:params:xml:ns:asn-1.0'
            })

        self.number = numbers