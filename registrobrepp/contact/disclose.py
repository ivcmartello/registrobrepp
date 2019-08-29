from eppy.xmldict import XmlDictObject

from registrobrepp.contact.infotype import InfoType


class Disclose(XmlDictObject):
    def __init__(self, flag: bool = False, name_loc: bool = False, name_int: bool = False, org_loc: bool = False,
                 org_int: bool = False, addr_loc: bool = False, addr_int: bool = False, voice: bool = False,
                 fax: bool = False, email: bool = False):
        super(Disclose, self).__init__()

        tloc = {'@type': InfoType.LOC.value}
        tint = {'@type': InfoType.INT.value}

        self['@flag'] = '0'
        if flag:
            self['@flag'] = '1'

        if name_loc:
            self.name = tloc
        elif name_int:
            self.name = tint

        if org_loc:
            self.org = tloc
        elif org_int:
            self.org = tint

        if addr_loc:
            self.addr = tloc
        elif addr_int:
            self.addr = tint

        if voice:
            self.voice = {}

        if fax:
            self.fax = {}

        if email:
            self.email = {}
