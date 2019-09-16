from eppy.xmldict import XmlDictObject


class AddAsn(XmlDictObject):
    def __init__(self, contacts: list, asins: list = None):
        dct = {
            'contact': contacts,
            'asIn': asins
        }
        super(AddAsn, self).__init__(initdict=dct)
