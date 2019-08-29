from eppy.xmldict import XmlDictObject


class Property(XmlDictObject):
    def __init__(self, text):
        super(Property, self).__init__()
        self['_text'] = text