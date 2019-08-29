from eppy.doc import EppDoc


class Smd(EppDoc):
    _path = ('smd:encodedSignedMark', )

    def __init__(self, data: str):
        dct = {'_text': data}

        super(Smd, self).__init__(dct)
