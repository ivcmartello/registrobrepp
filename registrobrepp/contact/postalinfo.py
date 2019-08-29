from eppy.xmldict import XmlDictObject

from registrobrepp.contact.addr import Addr
from registrobrepp.contact.infotype import InfoType


class PostalInfo(XmlDictObject):
    def __init__(self, infotype: InfoType, name: str, address: Addr, organization: str = None):
        super(PostalInfo, self).__init__()
        self['@type'] = infotype.value
        self.name = name
        self.org = organization
        self.addr = address

    @staticmethod
    def build(name: str, address: Addr, organization: str = None, international: bool = False):
        if international:
            return PostalInfo(InfoType.INT, name, address, organization)
        return PostalInfo(InfoType.LOC, name, address, organization)
