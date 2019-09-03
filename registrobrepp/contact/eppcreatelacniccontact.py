from eppy.doc import EppDoc

from registrobrepp.common.language import Language


class EppCreateLacnicContact(EppDoc):
    _path = ('lacniccontact:create', )

    def __init__(self, password: str, reminder: str = 'Default', language: Language = Language.PT):
        dct = {
            'lacniccontact:create': {
                'password': password,
                'reminder': reminder,
                'language': language.value
            },
        }
        extra_nsmap = {'lacniccontact': 'urn:ietf:params:xml:ns:lacniccontact-1.0'}
        super(EppCreateLacnicContact, self).__init__(dct=self.annotate(dct), extra_nsmap=extra_nsmap)
