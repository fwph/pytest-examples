import yaml
import os


def pytest_generate_tests(metafunc):
    test_data_path = os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            'test_cases.yaml')

    if metafunc.function == test_datadriven_addition:
        with open(test_data_path, 'r') as infile:
            param_names, *test_cases = yaml.safe_load(infile)
        metafunc.parametrize(param_names,
                             test_cases)


def test_datadriven_addition(x, y, ans):
    assert x + y == ans
