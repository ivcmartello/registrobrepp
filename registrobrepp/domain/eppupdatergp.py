import datetime

from eppy.doc import EppDoc


class EppUpdateRgp(EppDoc):
    _path = ('rgp:update',)

    def __init__(self, predata: str, postdata: str, deltime: datetime, restime: datetime, resreason: str,
                 statements: list, other: str):
        dct = {
            'rgp:update': {
                'restore': {
                    '@op': 'report',
                    'report': {
                        'preData': predata,
                        'postData': postdata,
                        'delTime': deltime.strftime('%Y-%m-%dT%H:%M:%S.0Z'),
                        'resTime': restime.strftime('%Y-%m-%dT%H:%M:%S.0Z'),
                        'resReason': resreason,
                        'statement': statements,
                        'other': other
                    },
                },
            },
        }

        super(EppUpdateRgp, self).__init__(dct)
