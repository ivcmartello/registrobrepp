from eppy.xmldict import XmlDictObject

from registrobrepp.ipnetwork.iprange import IpRange


class ReverseDns(XmlDictObject):
    def __init__(self, iprange: IpRange, hostnames: list):
        dct = {
            'ipRange': iprange,
            'hostName': hostnames,
        }
        super(ReverseDns, self).__init__(initdict=dct)
