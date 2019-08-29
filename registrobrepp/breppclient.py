from eppy.client import EppClient


class BrEppClient(EppClient):

    def __init__(self, host=None, port=700, ssl_enable=True, ssl_keyfile=None, ssl_certfile=None, ssl_cacerts=None,
                 ssl_version=None, ssl_ciphers=None, ssl_validate_hostname=True, socket_timeout=60,
                 socket_connect_timeout=15, ssl_validate_cert=True):

        super(BrEppClient, self).__init__(host, port, ssl_enable, ssl_keyfile, ssl_certfile, ssl_cacerts, ssl_version,
                                          ssl_ciphers, ssl_validate_hostname, socket_timeout, socket_connect_timeout,
                                          ssl_validate_cert)

        self._objuris = [
            'urn:ietf:params:xml:ns:domain-1.0',
            'urn:ietf:params:xml:ns:contact-1.0'
        ]

        self._extra_ext_uris = [
            'urn:ietf:params:xml:ns:brdomain-1.0',
            'urn:ietf:params:xml:ns:brorg-1.0',
            'urn:ietf:params:xml:ns:secDNS-1.0',
            'urn:ietf:params:xml:ns:secDNS-1.1'
        ]

    def login(self, clID, pw, newPW=None, raise_on_fail=True,
              obj_uris=None, extra_obj_uris=None, extra_ext_uris=None, clTRID=None):

        objuris = self._objuris
        if obj_uris:
            objuris += obj_uris

        extraexturis = self._extra_ext_uris
        if extra_ext_uris:
            extraexturis += extra_ext_uris

        return super(BrEppClient, self).login(clID, pw, newPW, raise_on_fail, objuris, extra_obj_uris, extraexturis,
                                              clTRID)
