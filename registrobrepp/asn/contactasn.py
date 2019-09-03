from eppy.xmldict import XmlDictObject

from registrobrepp.asn.contactasntype import ContactAsnType


class ContactAsn(XmlDictObject):
    def __init__(self, contactType: ContactAsnType, info: str):
        dct = {
            '@type': contactType.value,
            '_text': info
        }
        super(ContactAsn, self).__init__(initdict=dct)

    @staticmethod
    def build(info: str, routing: bool = False):
        if routing:
            return ContactAsn(ContactAsnType.ROUTING, info)
        return ContactAsn(ContactAsnType.SECURITY, info)

