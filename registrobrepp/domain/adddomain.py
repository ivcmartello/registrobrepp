from eppy.xmldict import XmlDictObject

from .contact import Contact
from registrobrepp.domain.ns import Ns
from registrobrepp.status import Status


class AddDomain(XmlDictObject):
    def __init__(self, ns: Ns = None, contact: Contact = None, status: Status = None):
        super(AddDomain, self).__init__()

        self.ns = ns
        self.contact = contact
        self.status = status
