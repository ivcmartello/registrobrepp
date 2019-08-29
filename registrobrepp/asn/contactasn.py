from eppy.xmldict import XmlDictObject

from registrobrepp.asn.contactasntype import ContactAsnType


class ContactAsn(XmlDictObject):
    def __init__(self, contactType: ContactAsnType, info: str):
        super(ContactAsn, self).__init__()

        self['@type'] = contactType.value
        self['_text'] = info

    @staticmethod
    def build(info: str, routing: bool = False):
        if routing:
            return ContactAsn(ContactAsnType.ROUTING, info)
        return ContactAsn(ContactAsnType.SECURITY, info)
