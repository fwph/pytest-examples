import pytest


@pytest.mark.parametrize(['x', 'y', 'ans'],
                         [(1, 1, 2),
                          (1, 2, 3),
                          (1, 3, 4),
                          (1, 4, 5)])
def test_addition(x, y, ans):
    assert x + y == ans


@pytest.mark.parametrize(['x', 'y', 'ans'],
                         [(1, 1, 2),
                          pytest.mark.xfail((1, 1, 3), reason='bad mojo'),
                          ('ug', 'ly', 'ugly'),
                          pytest.mark.skip(('cth', 'ulu', 'cthulu'))],
                         ids=['good', 'bad', 'ugly', 'evil'])
def test_addition_extra(x, y, ans):
    assert x + y == ans
