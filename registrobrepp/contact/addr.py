from eppy.xmldict import XmlDictObject


class Addr(XmlDictObject):
    def __init__(self, street1: str, street2: str, city: str, cc: str, street3: str = None, sp: str = None,
                 pc: str = None):
        streets = [street1, street2]
        if street3:
            streets.append(street3)
        dct = {
            'street': streets,
            'city': city,
            'sp': sp,
            'pc': pc,
            'cc': cc
        }
        super(Addr, self).__init__(initdict=dct)
