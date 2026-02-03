from example_calculator import calculate_accuracy, calculate_distance, calculate_sensitivity, calculate_specificity


def test_sensitivity_basic():
    result = calculate_sensitivity(3, 2)
    assert result == 0.6


def test_specificity_basic_1():
    result = calculate_specificity(10, 5)
    assert result == 0.5


def test_specificity_basic_2():
    result = calculate_specificity(10, 0)
    assert result == 0.0


def test_calculate_distance():
    acc = 0.75
    result = calculate_distance(acc)
    assert result == 0.25


def test_calculate_accuracy():
    sn = 0.8
    sp = 0.6
    result = calculate_accuracy(sn, sp)
    assert result == 0.7


def test_placeholder():
    assert True


# This is a placeholder test file. Replace with actual tests.
