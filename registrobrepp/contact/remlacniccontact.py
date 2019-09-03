from eppy.xmldict import XmlDictObject


class RemLacnicContact(XmlDictObject):
    def __init__(self, properties: list):
        dct = {
            'property': properties
        }
        super(RemLacnicContact, self).__init__(initdict=dct)
