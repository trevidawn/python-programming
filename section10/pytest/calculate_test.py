import pytest

import calculation

release_name = 'lesson'


def test_add_num_and_double():
    cal = calculation.Cal()
    assert cal.add_num_and_double(1, 1) != 4


class TestCal(object):
    @classmethod
    def setup_class(cls):
        print('START')
        cls.cal = calculation.Cal()

    def teardown_class(cls):
        print('END')
        del cls.cal

    def setup_method(self, method):
        print('method={}'.format(method.__name__))
        # self.cal = calculation.Cal()

    def teardown_method(self, method):
        print('method={}'.format(method.__name__))
        # del self.cal

    def test_add_num_and_double(self):
        assert self.cal.add_num_and_double(1, 1) == 4

    def test_add_num_and_double_raise(self):
        with pytest.raises(ValueError):
            self.cal.add_num_and_double('1', '1')


if __name__ == '__main__':
    pytest.main()
