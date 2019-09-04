from eppy.xmldict import XmlDictObject


class ChgIpNetwork(XmlDictObject):
    def __init__(self, organization: str, alloctype: str, asn: int):
        dct = {
            'organization': organization,
            'allocType': alloctype,
            'asn': asn
        }
        super(ChgIpNetwork, self).__init__(initdict=dct)
