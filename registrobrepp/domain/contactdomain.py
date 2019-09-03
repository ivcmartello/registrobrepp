from eppy.xmldict import XmlDictObject

from registrobrepp.domain.contactdomaintype import ContactDomainType


class ContactDomain(XmlDictObject):
    def __init__(self, contactType: ContactDomainType, info: str):
        dct = {
            '@type': contactType.value,
            '_text': info
        }
        super(ContactDomain, self).__init__(initdict=dct)

    @staticmethod
    def build(info: str, admin: bool = False, tech: bool = False):
        if admin:
            return ContactDomain(ContactDomainType.ADMIN, info)
        elif tech:
            return ContactDomain(ContactDomainType.TECH, info)
        return ContactDomain(ContactDomainType.BILLING, info)



