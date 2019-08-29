from eppy.xmldict import XmlDictObject


class ChgLacnicContact(XmlDictObject):
    def __init__(self, password: str, reminder: str = 'Default', language: str = 'pt'):
        super(ChgLacnicContact, self).__init__()

        self.password = password
        self.reminder = reminder
        self.language = language
