from eppy.xmldict import XmlDictObject

from registrobrepp.contact.contactbrorg import ContactBrOrg


class AddBrOrg(XmlDictObject):
    def __init__(self, contact: ContactBrOrg):
        dct = {
            'contact': contact
        }
        super(AddBrOrg, self).__init__(initdict=dct)