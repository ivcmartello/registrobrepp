from eppy.xmldict import XmlDictObject


class Statement(XmlDictObject):
    def __init__(self, text: str, lang: str = None):
        super(Statement).__init__()
        self['@lang'] = lang
        self['_text'] = text
