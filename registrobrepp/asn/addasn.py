from eppy.xmldict import XmlDictObject


class AddAsn(XmlDictObject):
    def __init__(self, contacts: list, asins: list):
        super(AddAsn, self).__init__()

        self.contact = contacts
        self.asIn = asins
