from eppy.doc import EppDoc


class EppCreateBrOrg(EppDoc):
    _path = ('brorg:create',)

    def __init__(self, organization: str, contacts: list, responsible: str):
        dict = {
            'brorg:create': {
                'organization': organization,
                'contact': contacts,
                'responsible': responsible
            }
        }

        super(EppCreateBrOrg, self).__init__(dict, extra_nsmap={'brorg': 'urn:ietf:params:xml:ns:brorg-1.0'})
