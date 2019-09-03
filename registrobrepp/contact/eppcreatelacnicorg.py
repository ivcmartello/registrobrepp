from eppy.doc import EppDoc

from registrobrepp.contact.orgtype import OrgType
from registrobrepp.contact.resourcesclass import ResourcesClass


class EppCreateLacnicOrg(EppDoc):
    _path = ('lacnicorg:create', )

    def __init__(self, orgtype: OrgType, password: str, eppips: list, renewaltypes: list, resourcesclass: ResourcesClass):
        dct = {
            'lacnicorg:create': {
                'type': orgtype.value,
                'eppPassword': password,
                'eppIP': eppips,
                'renewalType': [v.value for v in renewaltypes],
                'resourcesClass': resourcesclass.value
            },
        }
        extra_nsmap = {'lacnicorg': 'urn:ietf:params:xml:ns:lacnicorg-1.0'}
        super(EppCreateLacnicOrg, self).__init__(dct=self.annotate(dct), extra_nsmap=extra_nsmap)
