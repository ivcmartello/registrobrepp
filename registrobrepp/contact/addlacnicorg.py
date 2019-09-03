from eppy.xmldict import XmlDictObject

from registrobrepp.contact.renewaltype import RenewalType


class AddLacnicOrg(XmlDictObject):
    def __init__(self, ips, renewaltype: RenewalType):
        dct = {
            'eppIP': ips,
            'renewalType': renewaltype.value
        }
        super(AddLacnicOrg, self).__init__(initdict=dct)