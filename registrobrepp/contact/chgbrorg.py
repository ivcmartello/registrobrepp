import datetime

from eppy.xmldict import XmlDictObject


class ChgBrOrg(XmlDictObject):
    def __init__(self, responsible: str, exdate: datetime, suspended: bool = False):
        dct = {
            'responsible': responsible,
            'exDate': exdate.strftime('%Y-%m-%dT%H:%M:%S.0Z'),
            'suspended': str(suspended).lower()
        }
        super(ChgBrOrg, self).__init__(initdict=dct)
