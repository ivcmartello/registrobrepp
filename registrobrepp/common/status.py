from enum import Enum

from eppy.xmldict import XmlDictObject

from registrobrepp.common.language import Language
from registrobrepp.common.statustype import StatusDefRegType, StatusDomainType, StatusContactType


class StatusBase(XmlDictObject):
    def __init__(self, s: Enum, info: str = None, lang: Language = None):
        super(StatusBase, self).__init__()
        self['@s'] = s.value
        if lang:
            self['@lang'] = lang.value
        self['_text'] = info


class StatusDefReg(StatusBase):
    def __init__(self, s: StatusDefRegType, info: str = None, lang: Language = None):
        super(StatusDefReg, self).__init__(s, info, lang)


class StatusDomain(StatusBase):
    def __init__(self, s: StatusDomainType, info: str = None, lang: Language = None):
        super(StatusDomain, self).__init__(s, info, lang)


class StatusContact(StatusBase):
    def __init__(self, s: StatusContactType, info: str = None, lang: Language = None):
        super(StatusContact, self).__init__(s, info, lang)
