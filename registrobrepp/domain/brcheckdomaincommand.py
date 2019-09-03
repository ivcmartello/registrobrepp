from eppy.doc import EppCheckDomainCommand


class BrEppCheckDomainCommand(EppCheckDomainCommand):
    def __init__(self, names: list):
        dct = {
            'epp': {
                'command': {
                    'check': {
                        'domain:check': {
                            'name': names
                        }
                    }
                }
            }
        }
        extra_nsmap = {'brdomain': 'urn:ietf:params:xml:ns:brdomain-1.0'}
        super(BrEppCheckDomainCommand, self).__init__(dct=self.annotate(dct), extra_nsmap=extra_nsmap)
