from eppy.xmldict import XmlDictObject

from registrobrepp.ipnetwork.iprange import IpRange


class DsData(XmlDictObject):
    def __init__(self, iprange: IpRange, keytag: str, alg: int, digesttype: int, digest: str):
        dct = {
            'ipRange': iprange,
            'keyTag': keytag,
            'alg': alg,
            'digestType': digesttype,
            'digest': digest
        }
        super(DsData, self).__init__(initdict=dct)
