from eppy.doc import EppDeleteDomainCommand


class BrEppDeleteDomainCommand(EppDeleteDomainCommand):
    def __init__(self, name: str):
        dct = {
            'epp': {
                'command': {
                    'delete': {
                        'domain:delete': {
                            'name': name
                        }
                    }
                }
            }
        }
        super(BrEppDeleteDomainCommand, self).__init__(dct=self.annotate(dct))
