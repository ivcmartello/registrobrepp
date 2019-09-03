from eppy.xmldict import XmlDictObject

from registrobrepp.contact.eppstatus import EppStatus
from registrobrepp.contact.orgtype import OrgType
from registrobrepp.contact.resourcesclass import ResourcesClass


class ChgLacnicOrg(XmlDictObject):
    def __init__(self, orgtype: OrgType, status: EppStatus, epppassword: str, resourcesclass: ResourcesClass):
        dct = {
            'type': orgtype.value,
            'eppStatus': status.value,
            'eppPassword': epppassword,
            'resourcesClass': resourcesclass.value
        }
        super(ChgLacnicOrg, self).__init__(initdict=dct)
