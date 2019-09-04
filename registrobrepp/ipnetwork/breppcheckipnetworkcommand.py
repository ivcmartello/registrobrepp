from eppy.doc import EppCheckCommand


class BrEppCheckIpNetworkCommand(EppCheckCommand):
    def __init__(self, startaddress: str, endaddress: str):
        dct = {
            'epp': {
                'command': {
                    'check': {
                        'ipnetwork:check': {
                            'ipRange': {
                                '@version': 'v4',
                                'startAddress': startaddress,
                                'endAddress': endaddress
                            }
                        }
                    }
                }
            }
        }
        extra_nsmap = {'ipnetwork': 'urn:ietf:params:xml:ns:ipnetwork-1.0'}
        super(BrEppCheckIpNetworkCommand, self).__init__(dct=self.annotate(dct), extra_nsmap=extra_nsmap)
