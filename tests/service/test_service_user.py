import pytest

from src.service.service_user import ServiceUser


class TestServiceUser:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.service_user = ServiceUser()

    def test_add_user_success(self):
        result = self.service_user.add_user("Camilla", "Cargo Teste")
        assert result == "User added"

    def test_add_user_empty_string_fail(self):
        result = self.service_user.add_user("", "Cargo Teste")
        assert result == "Empty parameters not allowed"

    def test_add_user_invalid_string_fail(self):
        result = self.service_user.add_user(3, "Cargo Teste")
        assert result == "Invalid parameters"