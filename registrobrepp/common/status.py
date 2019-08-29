from eppy.xmldict import XmlDictObject


class Status(XmlDictObject):
    def __init__(self, s: str, info: str = None, lang: str = None):
        super(Status, self).__init__()

        self['@s'] = s
        self['@lang'] = lang
        self['_text'] = info
