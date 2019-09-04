from eppy.doc import EppInfoCommand

from registrobrepp.ipnetwork.iprange import IpRange


class BrEppInfoIpNetworkCommand(EppInfoCommand):
    def __init__(self, iprange: IpRange, roid: str):
        dct = {
            'epp': {
                'command': {
                    'info': {
                        'ipnetwork:info': {
                            'ipRange': iprange,
                            'roid': roid
                        }
                    }
                }
            }
        }
        extra_nsmap = {'ipnetwork': 'urn:ietf:params:xml:ns:ipnetwork-1.0'}
        super(BrEppInfoIpNetworkCommand, self).__init__(dct=self.annotate(dct), extra_nsmap=extra_nsmap)
