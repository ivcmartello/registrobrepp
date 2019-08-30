from eppy.xmldict import XmlDictObject

from registrobrepp.contact.contactbrorgtype import ContactBrOrgType


class ContactBrOrg(XmlDictObject):
    def __init__(self, contactType: ContactBrOrgType, info: str):
        super(ContactBrOrg, self).__init__()

        self['@type'] = contactType.value
        self['_text'] = info

    @staticmethod
    def build(info: str, admin: bool = False, member: bool = False):
        if admin:
            return ContactBrOrg(ContactBrOrgType.ADMIN, info)
        elif member:
            return ContactBrOrg(ContactBrOrgType.MEMBER, info)
        return ContactBrOrg(ContactBrOrgType.BILLING, info)
