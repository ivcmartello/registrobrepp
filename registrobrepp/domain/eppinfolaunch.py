from eppy.doc import EppDoc


class EppInfoLaunch(EppDoc):
    _path = ('launch: info', )

    def __init__(self, phase: str, applicationid: str):
        dct = {
            'launch:info': {
                '@includeMark': 'true',
                'phase': phase,
                'applicationID': applicationid
            },
        }
        super(EppInfoLaunch, self).__init__(dct=self.annotate(dct))
