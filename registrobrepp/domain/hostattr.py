from eppy.xmldict import XmlDictObject


class HostAttr(XmlDictObject):
    def __init__(self, hostname: str, hostaddrs: list = None):
        dct = {
            'hostName': hostname,
            'hostAddr': hostaddrs
        }
        super(HostAttr, self).__init__(initdict=dct)
