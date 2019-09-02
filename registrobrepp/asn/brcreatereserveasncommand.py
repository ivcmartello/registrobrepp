from eppy.doc import EppCommand


class BrEppCreateReserveAsnCommand(EppCommand):
    _path = ('epp', 'command', 'create', 'asnReserve:create')

    def __init__(self, startAsn: int, endAsn: int, organization: str, comment: str = None):
        super(BrEppCreateReserveAsnCommand, self).__init__(extra_nsmap={'asnReserve': 'urn:ietf:params:xml:ns:asnReserve-1.0'})

        self.startASN = startAsn
        self.endASN = endAsn
        self.organization = organization
        self.comment = comment
