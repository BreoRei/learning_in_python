# Возьмите 1-3 задания из тех, что были на прошлых семинарах или в домашних заданиях. Напишите к ним тесты.
# 2-5 тестов на задание в трёх вариантах:
# - unittest,
# - pytest.

import unittest
from matrix import Matrix


class TestCleanText(unittest.TestCase):
    def setUp(self):
        self.m1 = Matrix([[1, 2, 4, 2], [3, 4, 5, 1], [7, 8, 6, 4], [2, 4, 9, 1]])
        self.m2 = Matrix([[1, 2, 4, 2], [3, 4, 5, 1], [7, 8, 6, 4], [2, 4, 9, 1]])
        self.m3 = Matrix([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]])

    def test_step_1_equal(self):
        self.assertEqual(self.m1, self.m2)

    def test_step_2_gt(self):
        self.assertTrue(self.m1 > self.m3)

    def test_step_2_lt(self):
        self.assertTrue(self.m3 < self.m2)
        self.assertFalse(self.m2 < self.m1)


if __name__ == '__main__':
    unittest.main(verbosity=2)
