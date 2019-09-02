from eppy.doc import EppCommand


class BrEppDeleteReserveAsnCommand(EppCommand):
    _path = ('epp', 'command', 'delete', 'asnReserve:delete')

    def __init__(self, id: int):
        super(BrEppDeleteReserveAsnCommand, self).__init__(extra_nsmap={'asnReserve': 'urn:ietf:params:xml:ns:asnReserve-1.0'})

        self.id = id