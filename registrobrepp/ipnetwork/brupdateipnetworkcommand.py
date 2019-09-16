import datetime

from eppy.doc import EppUpdateCommand

from registrobrepp.ipnetwork.addipnetwork import AddIpNetwork
from registrobrepp.ipnetwork.aggripnetwork import AggrIpNetwork
from registrobrepp.ipnetwork.chgipnetwork import ChgIpNetwork
from registrobrepp.ipnetwork.remipnetwork import RemIpNetwork


class BrEppUpdateIpNetworkCommand(EppUpdateCommand):
    def __init__(self, roid: str, creationdate: datetime = None, add: AddIpNetwork = None, rem: RemIpNetwork = None,
                 chg: ChgIpNetwork = None, aggr: AggrIpNetwork = None):

        if not add and not rem and not chg:
            raise ValueError('At least one <ipnetwork:add>, <ipnetwork:rem>, or <ipnetwork:chg> element MUST be provided')

        cd = None
        if creationdate:
            cd = creationdate.strftime('%Y-%m-%dT%H:%M:%S.0Z')
        dct = {
            'epp': {
                'command': {
                    'update': {
                        'ipnetwork:update': {
                            'roid': roid,
                            'add': add,
                            'rem': rem,
                            'chg': chg,
                            'aggr': aggr,
                            'creation_date': cd
                        }
                    }
                }
            }
        }
        extra_nsmap = {'ipnetwork': 'urn:ietf:params:xml:ns:ipnetwork-1.0'}
        super(BrEppUpdateIpNetworkCommand, self).__init__(dct=self.annotate(dct), extra_nsmap=extra_nsmap)
