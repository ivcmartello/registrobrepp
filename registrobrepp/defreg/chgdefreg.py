import datetime

from eppy.xmldict import XmlDictObject

from registrobrepp.common.authinfo import AuthInfo


class ChgDefReg(XmlDictObject):
    def __init__(self, registrant: str, tm: str, tmcountry: str, tmdate: datetime, admincontact: str, authinfo: AuthInfo):
        dct = {
            'registrant': registrant,
            'tm': tm,
            'tmCountry': tmcountry,
            'tmDate': tmdate.strftime('%Y-%m-%d'),
            'adminContact': admincontact,
            'authInfo': authinfo
        }
        super(ChgDefReg, self).__init__(initdict=dct)