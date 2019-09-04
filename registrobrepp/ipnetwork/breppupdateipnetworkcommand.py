import datetime

from eppy.doc import EppUpdateCommand

from registrobrepp.ipnetwork.addipnetwork import AddIpNetwork
from registrobrepp.ipnetwork.chgipnetwork import ChgIpNetwork
from registrobrepp.ipnetwork.remipnetwork import RemIpNetwork


class BrEppUpdateIpNetworkCommand(EppUpdateCommand):
    def __init__(self, roid: str, creationdate: datetime, add: AddIpNetwork = None, rem: RemIpNetwork = None, chg: ChgIpNetwork = None):
        dct = {
            'epp': {
                'command': {
                    'update': {
                        'ipnetwork:update': {
                            'roid': roid,
                            'add': add,
                            'rem': rem,
                            'chg': chg,
                            'creation_date': creationdate.strftime('%Y-%m-%dT%H:%M:%S.0Z')
                        }
                    }
                }
            }
        }
        extra_nsmap = {'ipnetwork': 'urn:ietf:params:xml:ns:ipnetwork-1.0'}
        super(BrEppUpdateIpNetworkCommand, self).__init__(dct=self.annotate(dct), extra_nsmap=extra_nsmap)
