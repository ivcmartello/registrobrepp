from eppy.doc import EppDoc

from registrobrepp.domain.smd import Smd


class EppCreateLaunch(EppDoc):
    _path = ('launch:create', )

    def __init__(self, phase: str, smd: Smd = None):
        dct = {
            'launch:create': {
                'phase': phase,
            },
        }
        if smd:
            dct['launch:create']['smd:encodedSignedMark'] = smd
        super(EppCreateLaunch, self).__init__(dct=self.annotate(dct))
