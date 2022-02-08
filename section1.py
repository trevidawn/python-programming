import math

print('########################################################')
print('변수 선언')
print('########################################################')

# 변수와 타입 출력
num = 1
name = 'Mike'

print(num, type(num))
print(name, type(name))
print()
"""OUTPUT
1 <class 'int'>
Mike <class 'str'>
"""

# 다른 타입의 변수에 대입
print(id(num))
num = name
print(num, type(num), id(num))
print()
"""OUTPUT
140476005095728
Mike <class 'str'> 140476037824304
"""

# 타입 캐스팅
numStr = '1'
num = int(numStr)
print(num, type(num))
print()
"""OUTPUT
1 <class 'int'>
"""

# 형선언, python3.6부터 사용 가능, 강제성은 없는듯하다 따라서 쓰지 않는게 편하다
num: int = 1
name: str = '1'

print('########################################################')
print('# print')
print('########################################################')
print('Hi')
print('Hi', 'Mike')
print('Hi', 'Mike', sep=',')
print('Hi', 'Mike', sep=',', end='~!\n')
"""OUTPUT
Hi
Hi Mike
Hi,Mike
Hi,Mike~!
"""

print('########################################################')
print('# 수치')
print('########################################################')

# 연산
print(.6)
print(17 / 3)
print(17 // 3)
print(17 % 3)
print(5 ** 5)
print()
"""OUTPUT
0.6
5.666666666667
5
2
3125
"""

# math package
result = math.sqrt(25)
y = math.log2(10)
print(result)
print(y)
"""OUTPUT
5.0
3.321928094887362
"""


print('########################################################')
print(' 문자열')
print('########################################################')
# raw string : \n 무시
print(r'C:\name\name')
print()
"""OUTPUT
C:\name\name
"""

# 여러줄 출력
print("""
line1
line2
line3
""")
print()
"""OUTPUT

line1
line2
line3

"""

print("""\
line1
line2
line3\
""")
print()
"""OUTPUT
line1
line2
line3
"""

# 문자열 곱하기
print('Hi.' * 3)
print('Hi.' * 3 + 'Mike.')
print()
"""OUTPUT
Hi.Hi.Hi.
Hi.Hi.Hi.Mike.
"""

# 변수에 문자 리터럴 여러개 붙여서 쓰기
s = ('aaaaaaaaaaaaaaaaaaa'
     'bbbbbbbbbbbbbbbbbbbbbbbbbb'
     'qwerqwefasdfhaosdfho')
print(s)
print()
"""OUTPUT
aaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbqwerqwefasdfhaosdfho
"""

print('########################################################')
print('# 문자열의 인덱스와 슬라이스')
print('########################################################')

word = 'python'
print(word[0])
print(word[1])
print(word[2])
print(word[-1])
print(word[0:2])
print(word[2:5])
print(word[2:])
# print(word[100]) // index out of range
# word[0] = 'j' // error, str object does not support item assignment
print()
"""OUTPUT
p
y
t
n
py
tho
thon
"""

word = 'j' + word[1:]
print(word)
print(word[:])
"""OUTPUT
jython
jython
"""

print('########################################################')
print('# 문자열의 메서드')
print('########################################################')
s = 'My name is Mike. Hi Mike.'

is_start = s.startswith('My')
print(is_start)
is_start = s.startswith('X')
print(is_start)
print()
"""OUTPUT
True
False
"""

print(s.find('Mike'))  # 시작 index 번호, 앞에서 부터 찾음
print(s.rfind('Mike'))  # 시작 index 번호, 뒤에서 부터 찾음
print(s.count('Mike'))
print(s.capitalize())
print(s.title())
print(s.upper())
print(s.lower())
print(s.replace('Mike', 'Nancy'))
print()
"""OUTPUT
My name is mike. hi mike.
My Name Is Mike. Hi Mike.
MY NAME IS MIKE. HI MIKE.
my name is mike. hi mike.
My name is Nancy. Hi Nancy.
"""

print('########################################################')
print('# 문자열의 대입')
print('########################################################')
print('My name is {0} {1}'.format('Jun', 'B'))
print('My name is {1} {0}'.format('Jun', 'B'))
print('My name is {name} {family}'.format(name='Jun', family='B'))
print()
"""OUTPUT
My name is Jun B
My name is B Jun
My name is Jun B
"""

print('########################################################')
print('# f-strings')
print('########################################################')
# Python 3.6부터 format대신 f-strings를 쓸수있다.

a = 'a'
x, y, z = 1, 2, 3

print(f'a is {a}')
print(f'a is {x}, {y}, {z}')
print(f'a is {z}, {y}, {x}')

name = 'Jun'
family = 'B'
print(f'My name is {name} {family}. I am {family} {name}')
"""OUTPUT
a is a
a is 1, 2, 3
a is 3, 2, 1
My name is Jun B. I am B Jun
"""
