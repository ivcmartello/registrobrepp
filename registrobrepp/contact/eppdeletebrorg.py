from eppy.doc import EppDoc


class EppDeleteBrOrg(EppDoc):
    _path = ('brorg:delete',)

    def __init__(self, organization: str):
        dct = {
            'brorg:delete': {
                'organization': organization
            }
        }
        extra_nsmap = {'brorg': 'urn:ietf:params:xml:ns:brorg-1.0'}
        super(EppDeleteBrOrg, self).__init__(dct=self.annotate(dct), extra_nsmap=extra_nsmap)
