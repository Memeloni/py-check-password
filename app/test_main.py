import pytest


from app.main import check_password


@pytest.mark.parametrize("password, expected", [
    ("Pass@1", False),
    ("qwerty", False),
    ("Str@ng", False),
    ("Pass@word1", True),
    ("Pass@woed123345", False),
])
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
