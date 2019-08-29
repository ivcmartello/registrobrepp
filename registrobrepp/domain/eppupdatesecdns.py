from eppy.doc import EppDoc


class EppUpdateSecDns(EppDoc):
    _path = ('secDNS:update', )

    def __init__(self, keytag: str, alg: int, digesttype: int, digest: str):
        dct = {
            'secDNS:update': {
                '@urgent': 'true',
                'add': {
                    'dsData': {
                        'keyTag': keytag,
                        'alg': alg,
                        'digestType': digesttype,
                        'digest': digest
                    }
                }
            }
        }

        super(EppUpdateSecDns, self).__init__(dct)
