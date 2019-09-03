from eppy.xmldict import XmlDictObject


class Cd(XmlDictObject):
    def __init__(self, id: str, organization: str):
        dct = {
            'id': id,
            'organization': organization
        }
        super(Cd, self).__init__(initdict=dct)
