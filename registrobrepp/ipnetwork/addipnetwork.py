from eppy.xmldict import XmlDictObject


class AddIpNetwork(XmlDictObject):
    def __init__(self, dsdata: list, contact: list = None):
        dct = {
            'dsData': dsdata,
            'contact': contact
        }
        super(AddIpNetwork, self).__init__(initdict=dct)
