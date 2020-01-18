import pytest
from operations import SumOperation, DecOperation, DivisionOperation


def test_sum_operation():
	assert SumOperation().calculate(1, 2, 3) == 6


def test_dec_operation():
	assert DecOperation().calculate(1, 2, 3) == -4


def test_division_operation():
	with pytest.raises(ZeroDivisionError):
		DivisionOperation().calculate(16, 4, 2, 0)
	assert DivisionOperation().calculate(16, 4, 2, 1) == 2
