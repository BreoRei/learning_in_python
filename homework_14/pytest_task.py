import pytest
from matrix import Matrix


@pytest.fixture
def m1():
    return Matrix([[1, 2, 4, 2], [3, 4, 5, 1], [7, 8, 6, 4], [2, 4, 9, 1]])


@pytest.fixture
def m2():
    return Matrix([[1, 2, 4, 2], [3, 4, 5, 1], [7, 8, 6, 4], [2, 4, 9, 1]])


@pytest.fixture
def m3():
    return Matrix([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]])


def test_step_1_equal(m1, m2):
    assert m1 == m2


def test_step_2_gt(m1, m3):
    assert m1 > m3


def test_step_3_lt(m2, m3):
    assert m3 < m2


def test_step_3_mul(m2, m3):
    assert m2 + m3


if __name__ == '__main__':
    pytest.main(['-vv'])
