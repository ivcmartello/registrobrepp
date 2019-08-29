from eppy.xmldict import XmlDictObject


class Phone(XmlDictObject):
    def __init__(self, ext, number):
        super(Phone, self).__init__()

        self['@x'] = ext
        self['_text'] = number
