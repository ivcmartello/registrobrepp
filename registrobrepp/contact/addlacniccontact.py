from eppy.xmldict import XmlDictObject


class AddLacnicContact(XmlDictObject):
    def __init__(self, properties: list):
        dct = {
            'property': properties
        }
        super(AddLacnicContact, self).__init__(initdict=dct)
