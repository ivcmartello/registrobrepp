from eppy.xmldict import XmlDictObject


class AddIpNetwork(XmlDictObject):
    def __init__(self, reversedns: list = None, dsdata: list = None, contact: list = None):
        dct = {
            'reverseDNS': reversedns,
            'dsData': dsdata,
            'contact': contact
        }
        super(AddIpNetwork, self).__init__(initdict=dct)
