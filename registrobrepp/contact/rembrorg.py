from eppy.xmldict import XmlDictObject

from registrobrepp.contact.contactbrorg import ContactBrOrg


class RemBrOrg(XmlDictObject):
    def __init__(self, contact: ContactBrOrg):
        dct = {
            'contact': contact
        }
        super(RemBrOrg, self).__init__(initdict=dct)