from eppy.doc import EppDoc


class EppCreateLacnicContact(EppDoc):
    _path = ('lacniccontact:create', )

    def __init__(self, password: str, reminder: str = 'Default', language: str = 'pt'):
        dct = {
            'lacniccontact:create': {
                'password': password,
                'reminder': reminder,
                'language': language
            },
        }

        super(EppCreateLacnicContact, self).\
            __init__(dct, extra_nsmap={'lacniccontact': 'urn:ietf:params:xml:ns:lacniccontact-1.0'})
