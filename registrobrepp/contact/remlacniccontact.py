from eppy.xmldict import XmlDictObject


class RemLacnicContact(XmlDictObject):
    def __init__(self, properties: list):
        super(RemLacnicContact, self).__init__()

        self.property = properties
