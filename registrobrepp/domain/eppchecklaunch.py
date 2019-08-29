from eppy.doc import EppDoc

from registrobrepp.domain.launchtype import LaunchType


class EppCheckLaunch(EppDoc):
    _path = ('launch:check', )

    def __init__(self, launchtype: LaunchType, phase: str):
        dct = {
            'launch:check': {
                '@type': launchtype.value,
                'phase': phase,
            },
        }

        super(EppCheckLaunch, self).__init__(dct)

    @staticmethod
    def build(info: str, claim: bool = False):
        return EppCheckLaunch(LaunchType.CLAIMS, info)
