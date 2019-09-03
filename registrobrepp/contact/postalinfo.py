from eppy.xmldict import XmlDictObject

from registrobrepp.contact.addr import Addr
from registrobrepp.contact.infotype import InfoType


class PostalInfo(XmlDictObject):
    def __init__(self, infotype: InfoType, name: str, address: Addr, organization: str = None):
        dct = {
            '@type': infotype.value,
            'name': name,
            'org': organization,
            'addr': address
        }
        super(PostalInfo, self).__init__(initdict=dct)

    @staticmethod
    def build(name: str, address: Addr, organization: str = None, international: bool = False):
        if international:
            return PostalInfo(InfoType.INT, name, address, organization)
        return PostalInfo(InfoType.LOC, name, address, organization)
