from eppy.xmldict import XmlDictObject


class HostAddr(XmlDictObject):
    def __init__(self, ipaddr: str, iptype: str = 'v4'):
        dct = {
            '@ip': iptype,
            '_text': ipaddr
        }
        super(HostAddr, self).__init__(initdict=dct)
