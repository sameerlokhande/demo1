import pytest
from sum import calculate_operations

def test_addition():
    result = calculate_operations(5, 3)
    assert result["Addition"] == 8

def test_subtraction():
    result = calculate_operations(5, 3)
    assert result["Subtraction"] == 2

def test_multiplication():
    result = calculate_operations(5, 3)
    assert result["Multiplication"] == 15

def test_division():
    result = calculate_operations(5, 3)
    assert result["Division"] == pytest.approx(1.6666666666666667)

def test_division_by_zero():
    with pytest.raises(ValueError):
        calculate_operations(5, 0)
