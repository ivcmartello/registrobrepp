from eppy.xmldict import XmlDictObject


class Property(XmlDictObject):
    def __init__(self, text):
        dct = {
            '_text': text
        }
        super(Property, self).__init__(initdict=dct)
