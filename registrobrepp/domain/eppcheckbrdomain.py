from eppy.doc import EppDoc


class EppCheckBrDomain(EppDoc):
    _path = ('brdomain:check',)

    def __init__(self, organization: str):
        dict = {
            'brdomain:check': {
                'organization': organization
            }
        }

        super(EppCheckBrDomain, self).__init__(dict)
