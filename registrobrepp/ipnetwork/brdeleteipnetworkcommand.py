from eppy.doc import EppDeleteCommand


class BrEppDeleteIpNetworkCommand(EppDeleteCommand):
    def __init__(self, roid: str):
        dct = {
            'epp': {
                'command': {
                    'delete': {
                        'ipnetwork:delete': {
                            'roid': roid
                        }
                    }
                }
            }
        }
        extra_nsmap = {'ipnetwork': 'urn:ietf:params:xml:ns:ipnetwork-1.0'}
        super(BrEppDeleteIpNetworkCommand, self).__init__(dct=self.annotate(dct), extra_nsmap=extra_nsmap)
