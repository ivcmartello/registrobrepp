from eppy.doc import EppDoc


class EppCreateBrOrg(EppDoc):
    _path = ('brorg:create',)

    def __init__(self, organization: str, contacts: list, responsible: str = None):
        dct = {
            'brorg:create': {
                'organization': organization,
                'contact': contacts,
                'responsible': responsible
            }
        }
        extra_nsmap = {'brorg': 'urn:ietf:params:xml:ns:brorg-1.0'}
        super(EppCreateBrOrg, self).__init__(dct=self.annotate(dct), extra_nsmap=extra_nsmap)
