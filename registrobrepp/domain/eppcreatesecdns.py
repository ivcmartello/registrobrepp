from eppy.doc import EppDoc


class EppCreateSecDns(EppDoc):
    _path = ('secDNS:create',)

    def __init__(self, keytag: str, alg: int, digesttype: int, digest: str):
        dct = {
            'secDNS:create': {
                'dsData': {
                    'keyTag': keytag,
                    'alg': alg,
                    'digestType': digesttype,
                    'digest': digest
                },
            },
        }
        super(EppCreateSecDns, self).__init__(dct=self.annotate(dct))
