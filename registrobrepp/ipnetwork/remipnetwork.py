from eppy.xmldict import XmlDictObject


class RemIpNetwork(XmlDictObject):
    def __init__(self, dsdata: list, contact: list = None):
        dct = {
            'dsData': dsdata,
            'contact': contact
        }
        super(RemIpNetwork, self).__init__(initdict=dct)
