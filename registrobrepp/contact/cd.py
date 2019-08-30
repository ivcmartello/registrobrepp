from eppy.xmldict import XmlDictObject


class Cd(XmlDictObject):
    def __init__(self, id: str, organization: str):
        super(Cd, self).__init__()

        self.id = id
        self.organization = organization
