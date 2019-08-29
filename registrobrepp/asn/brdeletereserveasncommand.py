from eppy.doc import EppCommand


class BrEppDeleteReserveAsnCommand(EppCommand):
    _path = ('epp', 'command', 'delete', 'asnReserve:delete')

    def __init__(self, id: int):
        ex_nsmap = {'asnReserve': 'urn:ietf:params:xml:ns:asnReserve-1.0'}
        super(BrEppDeleteReserveAsnCommand, self).__init__(extra_nsmap=ex_nsmap)

        self.id = id