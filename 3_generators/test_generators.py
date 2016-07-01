def pytest_generate_tests(metafunc):
    if metafunc.function == test_addition:
        test_cases = [[1, 1, 2],
                      [1, 2, 3],
                      [1, 3, 4],
                      [1, 4, 5]]
        metafunc.parametrize(['x', 'y', 'ans'],
                             test_cases)


def test_addition(x, y, ans):
    assert x + y == ans
