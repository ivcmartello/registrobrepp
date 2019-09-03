from eppy.doc import EppDoc


class EppUpdateLaunch(EppDoc):
    _path = ('launch:update',)

    def __init__(self, phase: str, applicationid: str):
        dct = {
            'launch:update': {
                'phase': phase,
                'applicationID': applicationid
            }
        }
        super(EppUpdateLaunch, self).__init__(dct=self.annotate(dct))
