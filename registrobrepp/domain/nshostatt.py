from eppy.xmldict import XmlDictObject


class NsHostAtt(XmlDictObject):
    def __init__(self, hostsattr: list):
        dct = {
            'hostAttr': hostsattr,
        }
        super(NsHostAtt, self).__init__(initdict=dct)
