from eppy.doc import EppCreateCommand


class BrEppCreateAsnCommand(EppCreateCommand):
    _path = ('epp', 'command', 'create', 'asn:create')

    def __init__(self, number: int, organization: str, contacts: list, asIn: list = None, asOut: list = None):
        dct = {
            'epp': {
                'command': {
                    'create': {
                        'asn:create': {
                            'number': number,
                            'organization': organization,
                            'contact': contacts,
                            'asIn': asIn,
                            'asOut': asOut
                        }
                    }
                }
            }
        }
        extra_nsmap = {'asn': 'urn:ietf:params:xml:ns:asn-1.0'}
        super(BrEppCreateAsnCommand, self).__init__(dct=self.annotate(dct), extra_nsmap=extra_nsmap)
