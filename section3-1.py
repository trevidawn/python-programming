print('########################################################')
print('# 한 줄이 길어질 경우')
print('########################################################')
s = 'aaaaaaaaaaa' \
    'bbbbbbbbbbb'
print(s)
x = 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 \
    + 1 + 1 + 1 + 1 + 1
print(x)
x = (1 + 1 + 1 + 1 + 1 + 1 + 1 + 1
     + 1 + 1 + 1 + 1 + 1)
print(x)
print()
"""OUTPUT
aaaaaaaaaaabbbbbbbbbbb
13
13
"""

print('########################################################')
print('# if문')
print('########################################################')

x = 10

if x < 0:
    print('negative')
elif x == 0:
    print('zero')
elif x == 10:
    print("10")
elif x == 10:  # never execute
    print("1000")
else:
    print('positive')
print()
"""OUTPUT
10
"""

print('########################################################')
print('# 논리연산자')
print('########################################################')
a = 1
b = 1

print(a == b)
print(a != b)
print(a < b)
print(a > 0 and b > 0)
print(a > 0 or b > 0)
print()
"""OUTPUT
True
False
False
True
True
"""

print('########################################################')
print('# in, not')
print('########################################################')
y = [1, 2, 3]
x = 1

if x in y:
    print('in')
if 100 not in y:
    print('not in')
print()
"""OUTPUT
in
not in
"""

a = 1
b = 2
if not a == b:
    print('Not equal')
if a != b:
    print('Not equal')
print()
"""OUTPUT
Not equal
Not equal
"""

print('########################################################')
print('# 값이 들어있지 않다는 판정을 하는 테크닉')
print('########################################################')
is_ok = True
if is_ok:
    print('OK!')

is_ok = 0
if is_ok:
    print('OK!')
else:
    print('No!')

is_ok = ''
if is_ok:
    print("not empty")
else:
    print('empty')

is_ok = [1, 2, 3]
if is_ok:
    print('not empty')
else:
    print('empty')

print()
"""OUTPUT
OK!
No!
empty
not empty

다음 값은 false: False, 0, 0.0, '', (), {}, set()
"""

print('########################################################')
print('# None판정')
print('########################################################')
# Python에서 아무 값이 들어있지 않다면, None이라 함

is_empty = None
print(is_empty)
print(type(is_empty))

if is_empty == None:
    print('None')

if is_empty is None:
    print('None')

if is_empty is not None:
    print('not None')

print(1 == True)
print(None is True)

print()
"""OUTPUT
None
<class 'NoneType'>
None
None
True
False
# is 는 Object자체를 비교
"""


print('########################################################')
print('# while else')
print('########################################################')
count = 0
while count < 2:
    print(count)
    count += 1
else:
    print('done')

print()
"""OUTPUT
0
1
done

# break가 없을 때, else를 실행하고 종료
"""

count = 0
while count < 2:
    if count == 1:
        break
    print(count)
    count += 1
else:
    print('done')

print()
"""OUTPUT
0
"""

print('########################################################')
print('# input 함수')
print('########################################################')
# while True:
#     word = input('Enter:')
#     if word == 'ok':
#         break
#     print('next')
#
# while True:
#     if input('Enter:') == 'ok':
#         break
#     print('next')

print('########################################################')
print('# for문 list')
print('########################################################')
some_list = [10, 20, 30, 40, 50]

for i in some_list:
    print(i)
print()
"""OUTPUT
10
20
30
40
50
"""

for word in ['My', 'name', 'is', 'Mike']:
    print(word)
print()
"""OUTPUT
My
name
is
Mike
"""

for s in 'abcde':
    print(s)
print()
"""OUTPUT
a
b
c
d
e
"""


print('########################################################')
print('# for else')
print('########################################################')

for fruit in ['apple', 'banana', 'orange']:
    print(fruit)
else:
    print('I ate all!')
print()
"""OUTPUT
apple
banana
orange
I ate all!
"""

for fruit in ['apple', 'banana', 'orange']:
    if fruit == 'banana':
        print('stop eating')
        break
    print(fruit)
else:
    print('I ate all!')
print()
"""OUTPUT
apple
stop eating
"""

print('########################################################')
print('# range')
print('########################################################')
for i in range(2):
    print(i)
print()
"""OUTPUT
0
1
"""

for i in range(2, 4):
    print(i)
print()
"""OUTPUT
2
3
"""

for i in range(2, 10, 3):
    print(i)
print()
"""OUTPUT
2
5
8
"""

for _ in range(2):
    print('hello')
print()
"""OUTPUT
hello
hello
"""

print('########################################################')
print('# enumerate')
print('########################################################')

for i, fruit in enumerate(['apple', 'banana', 'orange']):
    print(i, fruit)
print()
"""OUTPUT
0 apple
1 banana
2 orange
"""

print('########################################################')
print('# zip')
print('########################################################')
days = ['Mon', 'Tue', 'Wed']
fruits = ['apple', 'banan', 'orange']
drinks = ['coffee', 'tea', 'beer']

for day, fruit, drink in zip(days, fruits, drinks):
    print(day, fruit, drink)
print()
"""OUTPUT
Mon apple coffee
Tue banan tea
Wed orange beer

# len 다르면 에러 발생 IndexError: list index out of range
"""

print('########################################################')
print('# 사전을 for문으로 처리하기')
print('########################################################')

d = {'x': 100, 'y': 200}
# key만
for v in d:
    print(v)
print()
"""OUTPUT
x
y
"""

# key, value 둘다
for k, v in d.items():
    print(k, ':', v)
print()
"""OUTPUT
x : 100
y : 200
"""

print(d.items())
print()
"""OUTPUT
dict_items([('x', 100), ('y', 200)])
"""