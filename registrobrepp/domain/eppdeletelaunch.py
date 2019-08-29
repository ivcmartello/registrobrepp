from eppy.doc import EppDoc


class EppDeleteLaunch(EppDoc):
    _path = ('launch:delete', )

    def __init__(self, phase: str, applicationid: str):
        dct = {
            'launch:delete': {
                'phase': phase,
                'applicationID': applicationid
            },
        }

        super(EppDeleteLaunch, self).__init__(dct)
