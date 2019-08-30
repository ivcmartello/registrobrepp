import datetime

from eppy.doc import EppCommand

from registrobrepp.asn.addasn import AddAsn
from registrobrepp.asn.chgasn import ChgAsn
from registrobrepp.asn.remasn import RemAsn


class BrEppUpdateAsnCommand(EppCommand):
    _path = ('epp', 'command', 'update', 'asn:update')

    def __init__(self, number: int, creationdate: datetime, add: AddAsn = None, rem: RemAsn = None, chg: ChgAsn = None):
        ex_nsmap = {'asn': 'urn:ietf:params:xml:ns:asn-1.0'}
        super(BrEppUpdateAsnCommand, self).__init__(extra_nsmap=ex_nsmap)

        self.number = number
        self.add = add
        self.rem = rem
        self.chg = chg
        self.creation_date = creationdate.strftime('%Y-%m-%dT%H:%M:%S.0Z')
