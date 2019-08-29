from unittest.mock import patch

import pytest
from eppy.exceptions import EppLoginError

from registrobrepp.breppclient import BrEppClient


class TestBrEppClient:

    def test_login(self, objuris, extraexturis, eppresponsecode1000):
        registrobr = BrEppClient()
        username = 'user'
        password = '123'
        ouris = ['uri:teste']
        euris = ['uri:teste']
        with patch('registrobrepp.breppclient.EppClient.login') as mock_login:
            mock_login.return_value = eppresponsecode1000
            resp = registrobr.login(username, password, obj_uris=ouris, extra_ext_uris=euris)

        mock_login.assert_called_with(username, password, None, True, objuris + ouris, None, extraexturis + euris, None)
        assert resp.success
        assert resp.code == '1000'
        assert resp.msg == 'Command completed successfully'

    def test_login_change_password(self, objuris, extraexturis, eppresponsecode1000):
        registrobr = BrEppClient()
        username = 'user'
        password = '123'
        new_password = '321'
        with patch('registrobrepp.breppclient.EppClient.login') as mock_login:
            mock_login.return_value = eppresponsecode1000
            resp = registrobr.login(username, password, new_password)

        mock_login.assert_called_with(username, password, new_password, True, objuris, None, extraexturis, None)
        assert resp.success
        assert resp.code == '1000'
        assert resp.msg == 'Command completed successfully'

    def test_login_invalid_user(self):
        registrobr = BrEppClient()
        with patch('registrobrepp.breppclient.EppClient.login', side_effect=EppLoginError('2200')):
            with pytest.raises(EppLoginError) as excinfo:
                registrobr.login('', '123')
            assert "2200" in str(excinfo.value)

            with pytest.raises(EppLoginError) as excinfo:
                registrobr.login('user', '')
            assert "2200" in str(excinfo.value)

            with pytest.raises(EppLoginError) as excinfo:
                registrobr.login('', '')
            assert "2200" in str(excinfo.value)

    def test_logout(self, eppresponsecode1500):
        registrobr = BrEppClient()
        with patch('registrobrepp.breppclient.EppClient.logout') as mock_logout:
            mock_logout.return_value = eppresponsecode1500
            resp = registrobr.logout()

        mock_logout.assert_called_once()
        assert resp.code == '1500'
        assert resp.msg == 'Command completed successfully; ending session'
