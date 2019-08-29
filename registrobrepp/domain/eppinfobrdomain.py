from eppy.doc import EppDoc


class EppInfoBrDomain(EppDoc):
    _path = ('brdomain:info', )

    def __init__(self, ticketnumber: str):
        dict = {
            'brdomain:info': {
                'ticketNumber': ticketnumber
            }
        }

        super(EppInfoBrDomain, self).__init__(dict)
