from eppy.doc import EppDoc


class EppInfoBrDomain(EppDoc):
    _path = ('brdomain:info', )

    def __init__(self, ticketnumber: str):
        dct = {
            'brdomain:info': {
                'ticketNumber': ticketnumber
            }
        }
        super(EppInfoBrDomain, self).__init__(dct=self.annotate(dct))
