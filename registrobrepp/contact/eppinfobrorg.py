from eppy.doc import EppDoc


class EppInfoBrOrg(EppDoc):
    _path = ('brorg:info',)

    def __init__(self, organization: str):
        dct = {
            'brorg:info': {
                'organization': organization
            }
        }
        extra_nsmap = {'brorg': 'urn:ietf:params:xml:ns:brorg-1.0'}
        super(EppInfoBrOrg, self).__init__(dct=self.annotate(dct), extra_nsmap=extra_nsmap)
