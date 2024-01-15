import pytest


def tryy(strr):
    return strr[::-1]


@pytest.fixture(scope="function", params=[("abc", "cba"), ("123", "321")])
def param_test(request):
    return request.param


def test_length_stats(param_test):
    (inputt, expected) = param_test
    res = tryy(inputt)
    print(f"res = {res}, expected = {expected}")
    assert res == expected
