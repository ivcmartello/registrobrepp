from eppy.doc import EppCreateCommand

from registrobrepp.ipnetwork.contactipnetwork import ContactIpNetwork
from registrobrepp.ipnetwork.dsdata import DsData
from registrobrepp.ipnetwork.iprange import IpRange
from registrobrepp.ipnetwork.reversedns import ReverseDns


class BrEppCreateIpNetworkCommand(EppCreateCommand):
    def __init__(self, iprange: IpRange, organization: str, alloctype: str, contact: ContactIpNetwork,
                 reversedns: ReverseDns, dsdata: DsData):
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
