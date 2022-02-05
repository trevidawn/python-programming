import math

print('########################################################')
print('# 1. 변수 선언')
print('########################################################')

num = 1
name = 'Mike'

print(num, type(num))
print(name, type(name))

# 변수의 타입 출력 type(variable)
print(num, type(num))
print(name, type(name))
# OUTPUT
# 1 <class 'int'>
# Mike <class 'str'>

# 다른 타입에 대입
num = name
print(num, type(num))

# 형변환
numStr = '1'
new_num = int(numStr)
print(new_num, type(new_num))

# 형선언, python3.6부터, 강제성은 없는듯하다 따라서 쓰지 않는게 편하다
num: int = 1
name: str = '1'
num = name
print(num, type(num))

print('########################################################')
print('# 2. print로 출력하기')
print('########################################################')
print('Hi')
print('Hi', 'Mike')
print('Hi', 'Mike', sep=',')
print('Hi', 'Mike', sep=',', end='~!\n')
# OUTPUT
# Hi
# Hi Mike
# Hi,Mike
# Hi,Mike~!

print('########################################################')
print('# 3. 수치')
print('########################################################')
print(.6)
print(17 / 3)
print(17 // 3)
print(17 % 3)
print(5 ** 5)
# OUTPUT
# 0.6
# 5.666666666667
# 5
# 2
# 3125

# math package
result = math.sqrt(25)
print(result)
y = math.log2(10)
print(y)
print(help(math))

print('########################################################')
print('# 4. 문자열')
print('########################################################')
print('hello')
print("hello")
print("I don't know")
print('I don\'t know')

print('hello.\nHow are you?')
print(r'C:\name\name')

print('###########')
print("""
line1
line2
line3
""")
print('###########')

print('###########')
print("""\
line1
line2
line3\
""")
print('###########')

print('###########')
print("""line1
line2
line3""")
print('###########')

print('Hi.' * 3)
print('Hi.' * 3 + 'Mike.')
print('Py''thon')

prefix = 'Py'
print(prefix + 'thon')

# 리터럴에 + 안쓰고 변수에 할당하는 케이스
s = ('aaaaaaaaaaaaaaaaaaa'
     'bbbbbbbbbbbbbbbbbbbbbbbbbb'
     'qwerqwefasdfhaosdfho')

print(s)

print('########################################################')
print('# 5. 문자열의 인덱스와 슬라이스')
print('########################################################')
word = 'python'
print(word[0])
print(word[1])
print(word[2])
print(word[-1])
print('###########')
print(word[0:2])
print(word[2:5])
print('###########')
print(word[2:])
# print(word[100]) // index out of range
# word[0] = 'j' // error, str object does not support item assignment
word = 'j' + word[1:]
print(word)
print(word[:])
n = len(word)
print(n)

print('########################################################')
print('# 6. 문자열의 메서드')
print('########################################################')
s = 'My name is Mike. Hi Mike.'
print(s)

is_start = s.startswith('My')
print(is_start)
is_start = s.startswith('X')
print(is_start)

print('###########')
print(s.find('Mike'))  # 시작 index 번호, 앞에서부터 찾음
print(s.rfind('Mike'))  # 시작 index 번호, 뒤에서부터 찾음
print(s.count('Mike'))
print(s.capitalize())
print(s.title())
print(s.upper())
print(s.lower())
print(s.replace('Mike', 'Nancy'))

print('########################################################')
print('# 7. 문자열의 대입')
print('########################################################')
print('My name is {0} {1}'.format('Jun', 'B'))
print('My name is {1} {0}'.format('Jun', 'B'))
print('My name is {name} {family}'.format(name='Jun', family='B'))

print('########################################################')
print('# 7. f-strings')
print('########################################################')
# Python 3.6부터 format대신 f-strings를 쓸수있다.
a = 'a'
print(f'a is {a}')
x, y, z = 1, 2, 3
print(f'a is {x}, {y}, {z}')
print(f'a is {z}, {y}, {x}')
name = 'Jun'
family = 'B'
print(f'My name is {name} {family}. I am {family} {name}')
