from eppy.xmldict import XmlDictObject


class IpRange(XmlDictObject):
    def __init__(self, startaddress: str, endaddress: str, version: str = 'v4'):
        dct = {
            '@version': version,
            'startAddress': startaddress,
            'endAddress': endaddress
        }
        super(IpRange, self).__init__(initdict=dct)
