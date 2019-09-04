from eppy.xmldict import XmlDictObject


class AddDefReg(XmlDictObject):
    def __init__(self, status: list):
        dct = {
            'status': status
        }
        super(AddDefReg, self).__init__(initdict=dct)
