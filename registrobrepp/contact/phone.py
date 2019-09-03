from eppy.xmldict import XmlDictObject


class Phone(XmlDictObject):
    def __init__(self, ext, number):
        dct = {
            '@x': ext,
            '_text': number
        }
        super(Phone, self).__init__(initdict=dct)
