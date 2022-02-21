import unittest

import calculation

release_name = 'lesson2'


class CalTest(unittest.TestCase):
    def setUp(self):
        print('setup')
        self.cal = calculation.Cal()

    def tearDown(self):
        print('clean up')
        del self.cal

    @unittest.skip('skip!!!')
    def test_add_num_and_double(self):
        self.assertEqual(self.cal.add_num_and_double(1, 1), 3)

    @unittest.skipIf(release_name == 'lesson', 'skip@@@')
    def test_add_num_and_double_raise(self):
        with self.assertRaises(ValueError):
            self.cal.add_num_and_double('1', '1')


if __name__ == '__main__':
    unittest.main()

# python calcuate_test.py
# Setup: test가 일어나기 전 수행
# TearDown: test가 실행된 후 수행
# OUTPUT
# setup
# clean up
# Fsetup
# clean up
# .
# ======================================================================
# FAIL: test_add_num_and_double (__main__.CalTest)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "/Users/user/PycharmProjects/udemy-python3/python_programming/section10/calculate_test.py", line 16, in test_add_num_and_double
#     self.assertEqual(self.cal.add_num_and_double(1, 1), 3)
# AssertionError: 4 != 3
#
# ----------------------------------------------------------------------
# Ran 2 tests in 0.001s
#
# FAILED (failures=1)

# OUTPUT = skip
# ss
# ----------------------------------------------------------------------
# Ran 2 tests in 0.000s
#
# OK (skipped=2)
