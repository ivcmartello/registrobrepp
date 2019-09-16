from eppy.xmldict import XmlDictObject


class AggrIpNetwork(XmlDictObject):
    def __init__(self, roid: str, hostnames: list):
        dct = {
            'roid': roid,
            'hostName': hostnames,
        }
        super(AggrIpNetwork, self).__init__(initdict=dct)