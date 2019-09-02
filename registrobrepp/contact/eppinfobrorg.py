from eppy.doc import EppDoc


class EppInfoBrOrg(EppDoc):
    _path = ('brorg:info',)

    def __init__(self, organization: str):
        dict = {
            'brorg:info': {
                'organization': organization
            }
        }

        super(EppInfoBrOrg, self).__init__(dict, extra_nsmap={'brorg': 'urn:ietf:params:xml:ns:brorg-1.0'})
