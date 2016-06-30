import pytest


@pytest.mark.xfail(reason='xfail mark example')
def test_xfailing():
    """ example of an xfail test """
    assert 2 == 3


@pytest.mark.xfail(reason='xfail mark example (passing)')
def test_xpassing():
    """ example of an xpass test """
    assert 3 == 3


@pytest.mark.skip(reason='let sleeping Old Ones lie')
def test_sleeper():
    print('I HAVE AWOKEN!')

    raise Exception('cthulu')
