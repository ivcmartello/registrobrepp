from eppy.doc import EppDoc


class EppCreateBrDomain(EppDoc):
    _path = ('brdomain:create', )

    def __init__(self, organization: str, flag1: str = None, flag2: str = None, flag3: str = None, autorenew: bool = False):
        rpf = None
        if flag1 or flag2 or flag3:
            rpf = {'@flag1': flag1, '@flag2': flag2, '@flag3': flag3}
        dct = {
            'brdomain:create': {
                'organization': organization,
                'releaseProcessFlags': rpf,
                'autoRenew': {'@active': '1' if autorenew else '0'}
            }
        }
        super(EppCreateBrDomain, self).__init__(dct=self.annotate(dct))
