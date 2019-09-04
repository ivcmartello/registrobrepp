from eppy.xmldict import XmlDictObject

from registrobrepp.ipnetwork.contactipnetworktype import ContactIpNetworkType


class ContactIpNetwork(XmlDictObject):
    def __init__(self, contactType: ContactIpNetworkType, info: str):
        dct = {
            '@type': contactType.value,
            '_text': info
        }
        super(ContactIpNetwork, self).__init__(initdict=dct)

    @staticmethod
    def build(info: str, admin: bool = False, tech: bool = False):
        if admin:
            return ContactIpNetwork(ContactIpNetworkType.ADMIN, info)
        elif tech:
            return ContactIpNetwork(ContactIpNetworkType.TECH, info)
        return ContactIpNetwork(ContactIpNetworkType.ABUSE, info)
