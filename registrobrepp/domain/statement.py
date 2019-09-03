from eppy.xmldict import XmlDictObject


class Statement(XmlDictObject):
    def __init__(self, text: str, lang: str = None):
        dct = {
            '@lang': lang,
            '_text': text
        }
        super(Statement, self).__init__(initdict=dct)
