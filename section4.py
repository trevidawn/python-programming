import sys
# import pkg.utils
from pkg.tools import utils as u
# from pkg.utils import say_twice
# from pkg.talk import human
# from pkg.talk import animal
from pkg.talk import *

print('########################################################')
print('# 커맨드라인 인수')
print('########################################################')

print(sys.argv)
print()
"""OUTPUT
['/Users/user/PycharmProjects/udemy-python3/python_programming/section4.py']
"""

print('########################################################')
print('# Import 문과 AS')
print('########################################################')

# r = pkg.utils.say_twice('hello')
r = u.say_twice('hello')

print('########################################################')
# 절대 경로와 상대 경로의 Import

print(human.sing())
# ..tools import utils -> 별로 추천하진 않는다.

print('########################################################')
# 애스터리스크의 import와 __init__.py, __all__의  의미

print(animal.sing())
print(animal.cry())

print('########################################################')
# ImportError의 쓰임

try:
    from pkg import utils
except ImportError:
    from pkg.tools import utils

utils.say_twice('word')

print('########################################################')
# setup.py로 패키지로 만들어 배부하기


print('########################################################')
# 내장 함수

print()

ranking = {
    'A': 100,
    'B': 85,
    'C': 95
}

print(sorted(ranking, key=ranking.get, reverse=True))


print('########################################################')
# 표준 라이브러리

s = "asdfqwefqwefqwerqweaasdf"

d = {}
for c in s:
    if c not in d:
        d[c] = 0
    d[c] += 1

print(d)

d = {}
for c in s:
    d.setdefault(c, 0)
    d[c] += 1

print(d)


from collections import defaultdict

d = defaultdict(int)

for c in s:
    d[c] += 1

print(d)


print('########################################################')
# 서드파티 라이브러리

# pip install termcolor
from termcolor import colored

print('test')
print(colored('test', 'red'))

