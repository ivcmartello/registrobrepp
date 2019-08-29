from eppy.xmldict import XmlDictObject

from registrobrepp.domain.contacttype import ContactType


class Contact(XmlDictObject):
    def __init__(self, contactType: ContactType, info: str):
        super(Contact, self).__init__()

        self['@type'] = contactType.value
        self['_text'] = info

    @staticmethod
    def build(info: str, admin: bool = False, tech: bool = False):
        if admin:
            return Contact(ContactType.ADMIN, info)
        if tech:
            return Contact(ContactType.TECH, info)
        return Contact(ContactType.BILLING, info)
