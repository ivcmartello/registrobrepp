from eppy.doc import EppDoc


class EppCheckBrOrg(EppDoc):
    _path = ('brorg:check',)

    def __init__(self, cds):
        dict = {
            'brorg:check': {
                'cd': cds
            }
        }

        super(EppCheckBrOrg, self).__init__(dict, extra_nsmap={'brorg': 'urn:ietf:params:xml:ns:brorg-1.0'})
