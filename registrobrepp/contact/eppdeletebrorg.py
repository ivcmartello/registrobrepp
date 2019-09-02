from eppy.doc import EppDoc


class EppDeleteBrOrg(EppDoc):
    _path = ('brorg:delete',)

    def __init__(self, organization: str):
        dict = {
            'brorg:delete': {
                'organization': organization
            }
        }

        super(EppDeleteBrOrg, self).__init__(dict, extra_nsmap={'brorg': 'urn:ietf:params:xml:ns:brorg-1.0'})
