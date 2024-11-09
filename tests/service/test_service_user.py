import pytest

from src.service.service_user import ServiceUser


class TestServiceUser:

    def test_add_user_success(self):
        self.service_user = ServiceUser()
        expected_result = "User added"
        result = self.service_user.add_user("Camilla", "QA Engineer")
        assert result == expected_result

    def test_add_user_empty_string_fail(self):
        self.service_user = ServiceUser()
        expected_result = "Empty parameters not allowed"
        result = self.service_user.add_user("", "QA Engineer")
        assert result == expected_result

    def test_add_user_invalid_string_fail(self):
        self.service_user = ServiceUser()
        expected_result = "Invalid parameters"
        result = self.service_user.add_user(3, "QA Engineer")
        assert result == expected_result

    def test_update_user(self):
        expected_result = "Eduardo"
        self.service_user = ServiceUser()
        self.service_user.add_user("Camilla", "QA Engineer")
        result = self.service_user.update_user("Camilla", expected_result)
        assert result.name == expected_result

    def test_remove_user(self):
        expected_result = "User removed"
        self.service_user = ServiceUser()
        self.service_user.add_user("Camilla", "QA Engineer")
        result = self.service_user.remove_user("Camilla", "QA Engineer")
        assert result == expected_result

    def test_get_user_job_success(self):
        expected_result = "QA Engineer"
        self.service_user = ServiceUser()
        self.service_user.add_user("Camilla", expected_result)
        result = self.service_user.get_user_by_name("Camilla")
        assert result == expected_result
        