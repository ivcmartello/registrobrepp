from eppy.xmldict import XmlDictObject


class NsHostObj(XmlDictObject):
    def __init__(self, hostsobj: list):
        dct = {
            'hostObj': hostsobj,
        }
        super(NsHostObj, self).__init__(initdict=dct)
