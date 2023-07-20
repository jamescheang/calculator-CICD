import src.calculator as calculator
import pytest


# TC0001 - Addition
@pytest.mark.parametrize(f"num1, num2, expected", [
    (-3, -2, -5), (-1, 0, -1), (1, 2, 3), (3, 4, 7)
])
def test_add(num1, num2, expected):
    assert calculator.add(num1, num2) == expected


# TC0002 - Subtraction
@pytest.mark.parametrize(f"num1, num2, expected", [
    (-3, -2, -1), (-1, 0, -1), (1, 2, -1), (3, 4, -1)
])
def test_subtract(num1, num2, expected):
    assert calculator.subtract(num1, num2) == expected


# TC0003 - Multiplication
@pytest.mark.parametrize(f"num1, num2, expected", [
    (-3, -2, 6), (-1, 0, 0), (1, 2, 2), (3, 4, 12)
])
def test_multiply(num1, num2, expected):
    assert calculator.multiply(num1, num2) == expected


# TC0004 - Division
@pytest.mark.parametrize(f"num1, num2, expected", [
    (-3, -2, 1.5), (-1, -1, 1), (1, 2, 0.5), (3, 4, 0.75)
])
def test_divide(num1, num2, expected):
    assert calculator.divide(num1, num2) == expected


# TC0005 - More than 2 numerical values
@pytest.mark.parametrize(f"num1, num2, num3, expected", [
    (-3, -2, -1, "Only 2 numerical values allowed."),
    (-1, 0, 1, "Only 2 numerical values allowed."),
    (1, 2, 3, "Only 2 numerical values allowed."),
    (3, 4, 5, "Only 2 numerical values allowed.")
])
def test_moreThan2(num1, num2, num3, expected):
    assert calculator.add(num1, num2, num3) == expected


# TC0006 - Less than 2 numerical values
@pytest.mark.parametrize(f"num1, expected", [
    (-3, "Only 2 numerical values allowed."),
    (-1, "Only 2 numerical values allowed."),
    (1, "Only 2 numerical values allowed."),
    (3, "Only 2 numerical values allowed.")
])
def test_lessThan2(num1, expected):
    assert calculator.add(num1) == expected


# TC0007 - Non-nunmerical values
@pytest.mark.parametrize(f"num1, num2, expected", [
    (-3, "a", "Non-numerical values NOT allowed."),
    (-1, "a", "Non-numerical values NOT allowed."),
    ("1a", "2b", "Non-numerical values NOT allowed."),
    (3, "a", "Non-numerical values NOT allowed.")
])
def test_alphaNumeric(num1, num2, expected):
    assert calculator.add(num1, num2) == expected


# TC0008 - Divide by 0
@pytest.mark.parametrize(f"num1, num2, expected", [
    (-3, 0, "Cannot divide by 0."),
    (-1, 0, "Cannot divide by 0."),
    (1, 0, "Cannot divide by 0."),
    (3, 0, "Cannot divide by 0.")
])
def test_divideBy0(num1, num2, expected):
    divideOutput = calculator.divide(num1, num2)
    assert divideOutput == expected
    assert type(divideOutput) == str
