print('########################################################')
print('# doctest')
print('########################################################')

class Cal(object):
    def add_num_and_double(self, x, y):
        """Add and double

        >>> c = Cal()
        >>> c.add_num_and_double(1, 1)
        45

        >>> c.add_num_and_double("1", "1")
        Traceback (most recent call last):
        ...
        ValueError
        """

        if type(x) is not int or type(y) is not int:
            raise ValueError
        result = x + y
        result *= 2
        return result


# OUTPUT
# Failed example:
#     c.add_num_and_double(1, 1)
# Expected:
#     45
# Got:
#     4
# **********************************************************************
# 1 items had failures:
#    1 of   2 in __main__.Cal.add_num_and_double
# ***Test Failed*** 1 failures.
#
# 종료 코드 0(으)로 완료된 프로세스


# doctest는 main에서만 사용
if __name__ == '__main__':
    import doctest

    doctest.testmod()

print('########################################################')
print('# configpaser')
print('########################################################')