from eppy.doc import EppDoc


class EppCheckBrOrg(EppDoc):
    _path = ('brorg:check',)

    def __init__(self, cds):
        dct = {
            'brorg:check': {
                'cd': cds
            }
        }
        extra_nsmap = {'brorg': 'urn:ietf:params:xml:ns:brorg-1.0'}
        super(EppCheckBrOrg, self).__init__(dct=self.annotate(dct), extra_nsmap=extra_nsmap)
