from eppy.xmldict import XmlDictObject


class ChgAsn(XmlDictObject):
    def __init__(self, organization: str):
        super(ChgAsn, self).__init__()

        self.organization = organization
