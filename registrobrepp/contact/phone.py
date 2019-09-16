from eppy.xmldict import XmlDictObject


class Phone(XmlDictObject):
    def __init__(self, number, ext: str = None):
        dct = {
            '@x': ext,
            '_text': number
        }
        super(Phone, self).__init__(initdict=dct)
