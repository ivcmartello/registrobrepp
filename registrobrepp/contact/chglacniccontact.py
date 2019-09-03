from eppy.xmldict import XmlDictObject

from registrobrepp.common.language import Language


class ChgLacnicContact(XmlDictObject):
    def __init__(self, password: str, reminder: str = 'Default', language: Language = Language.PT):
        dct = {
            'password': password,
            'reminder': reminder,
            'language': language.value
        }
        super(ChgLacnicContact, self).__init__(initdict=dct)
