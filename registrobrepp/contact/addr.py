from eppy.xmldict import XmlDictObject


class Addr(XmlDictObject):
    def __init__(self, street1: str, street2: str, city: str, cc: str, street3: str = None, sp: str = None,
                 pc: str = None):
        super(Addr, self).__init__()

        self.street = [street1, street2]
        if street3:
            self.street.append(street3)
        self.city = city
        self.sp = sp
        self.pc = pc
        self.cc = cc
