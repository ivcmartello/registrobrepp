from eppy.doc import EppCommand


class BrEppCreateAsnCommand(EppCommand):
    _path = ('epp', 'command', 'create', 'asn:create')

    def __init__(self, number: int, organization: str, contacts: list, asIn: list = None, asOut: list = None):
        super(BrEppCreateAsnCommand, self).__init__(extra_nsmap={'asn': 'urn:ietf:params:xml:ns:asn-1.0'})

        self.number = number
        self.organization = organization
        self.contact = contacts
        self.asIn = asIn
        self.asOut = asOut
