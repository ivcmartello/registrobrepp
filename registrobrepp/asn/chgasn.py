from eppy.xmldict import XmlDictObject


class ChgAsn(XmlDictObject):
    def __init__(self, organization: str):
        dct = {
            'organization': organization
        }
        super(ChgAsn, self).__init__(initdict=dct)
