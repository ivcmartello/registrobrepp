from eppy.doc import EppDoc

from registrobrepp.domain.chgbrdomain import ChgBrDomain


class EppUpdateBrDomain(EppDoc):
    _path = ('brdomain:update', )

    def __init__(self, ticketnumber: str = None, chg: ChgBrDomain = None):
        dct = {
            'brdomain:update': {
                'ticketNumber': ticketnumber,
                'chg': chg
            }
        }
        super(EppUpdateBrDomain, self).__init__(dct=self.annotate(dct))
