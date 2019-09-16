from eppy.xmldict import XmlDictObject


class RemAsn(XmlDictObject):
    def __init__(self, contacts: list, asouts: list = None):
        dct = {
            'contact': contacts,
            'asOut': asouts
        }
        super(RemAsn, self).__init__(initdict=dct)
