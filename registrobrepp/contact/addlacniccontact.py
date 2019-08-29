from eppy.xmldict import XmlDictObject


class AddLacnicContact(XmlDictObject):
    def __init__(self, properties: list):
        super(AddLacnicContact, self).__init__()

        self.property = properties
