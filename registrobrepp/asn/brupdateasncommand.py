import datetime

from eppy.doc import EppCommand

from registrobrepp.asn.addasn import AddAsn
from registrobrepp.asn.chgasn import ChgAsn
from registrobrepp.asn.remasn import RemAsn


class BrEppUpdateAsnCommand(EppCommand):
    _path = ('epp', 'command', 'update', 'asn:update')

    def __init__(self, number: int, creationdate: datetime, add: AddAsn = None, rem: RemAsn = None, chg: ChgAsn = None):
        dct = {
            'epp': {
                'command': {
                    'update': {
                        'asn:update': {
                            'number': number,
                            'add': add,
                            'rem': rem,
                            'chg': chg,
                            'creation_date': creationdate.strftime('%Y-%m-%dT%H:%M:%S.0Z')
                        }
                    }
                }
            }
        }
        extra_nsmap = {'asn': 'urn:ietf:params:xml:ns:asn-1.0'}
        super(BrEppUpdateAsnCommand, self).__init__(dct=self.annotate(dct), extra_nsmap=extra_nsmap)
