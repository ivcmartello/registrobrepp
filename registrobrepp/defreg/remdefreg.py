from eppy.xmldict import XmlDictObject


class RemDefReg(XmlDictObject):
    def __init__(self, status: list):
        dct = {
            'status': status
        }
        super(RemDefReg, self).__init__(initdict=dct)
