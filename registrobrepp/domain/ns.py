from eppy.xmldict import XmlDictObject


class Ns(XmlDictObject):
    def __init__(self, hosts: list):
        dct = {
            'hostObj': hosts
        }
        super(Ns, self).__init__(initdict=dct)
