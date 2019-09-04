from eppy.xmldict import XmlDictObject

from registrobrepp.domain.contactdomain import ContactDomain
from registrobrepp.domain.ns import Ns
from registrobrepp.common.status import StatusDomain


class RemDomain(XmlDictObject):
    def __init__(self, ns: Ns = None, contact: ContactDomain = None, status: StatusDomain = None):
        dct = {
            'ns': ns,
            'contact': contact,
            'status': status
        }
        super(RemDomain, self).__init__(initdict=dct)
