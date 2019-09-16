from eppy.doc import EppCreateCommand

from registrobrepp.ipnetwork.iprange import IpRange


class BrEppCreateIpNetworkCommand(EppCreateCommand):
    def __init__(self, iprange: IpRange, organization: str, alloctype: str = None, contact: list = None,
                 reversedns: list = None, dsdata: list = None):
        dct = {
            'epp': {
                'command': {
                    'create': {
                        'ipnetwork:create': {
                            'ipRange': iprange,
                            'organization': organization,
                            'allocType': alloctype,
                            'contact': contact,
                            'reverseDNS': reversedns,
                            'dsData': dsdata
                        }
                    }
                }
            }
        }
        extra_nsmap = {'ipnetwork': 'urn:ietf:params:xml:ns:ipnetwork-1.0'}
        super(BrEppCreateIpNetworkCommand, self).__init__(dct=self.annotate(dct), extra_nsmap=extra_nsmap)
