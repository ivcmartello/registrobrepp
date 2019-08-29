from eppy.xmldict import XmlDictObject


class Ns(XmlDictObject):
    def __init__(self, hosts: list):
        super(Ns, self).__init__()
        
        self.hostObj = hosts