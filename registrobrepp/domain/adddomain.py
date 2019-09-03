from eppy.xmldict import XmlDictObject

from registrobrepp.domain.contactdomain import ContactDomain
from registrobrepp.domain.ns import Ns
from registrobrepp.common.status import Status


class AddDomain(XmlDictObject):
    def __init__(self, ns: Ns = None, contact: ContactDomain = None, status: Status = None):
        dct = {
            'ns': ns,
            'contact': contact,
            'status': status
        }
        super(AddDomain, self).__init__(initdict=dct)
