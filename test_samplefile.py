import pytest
@pytest.fixture
def setup_and_teardown():
    print("launch browser")
    print("open app in browsers")
    yield
    print("logout")
    print("close the browser")


def test_login_with_valid_credential(setup_and_teardown):
    print("testing test_login_with_valid_credential")


def test_login_with_valid_email_and_invalid_password(setup_and_teardown):
    print("testing test_login_with_valid_email_and_invalid_password")