from eppy.xmldict import XmlDictObject


class RemAsn(XmlDictObject):
    def __init__(self, contacts: list, asouts: list):
        super(RemAsn, self).__init__()

        self.contact = contacts
        self.asOut = asouts
