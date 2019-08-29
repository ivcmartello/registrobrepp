from eppy.xmldict import XmlDictObject


class AuthInfo(XmlDictObject):
    def __init__(self, pw: str, roid: str = None):
        super(AuthInfo, self).__init__()

        self.pw = {'@roid': roid, '_text': pw}
