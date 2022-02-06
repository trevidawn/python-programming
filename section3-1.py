print('########################################################')
print('# 주석문')

print('XXXXX')
"""
test
setse
aset
"""
print('XXXXX')

# asdfasd

print('########################################################')
print('# 한 줄이 길어질 경우')

s = 'aaaaaaaaaaa' \
    'bbbbbbbbbbb'
print(s)

x = 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 \
    + 1 + 1 + 1 + 1 + 1

print(x)

x = (1 + 1 + 1 + 1 + 1 + 1 + 1 + 1
     + 1 + 1 + 1 + 1 + 1)

print(x)

print('########################################################')
print('# if문')

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

a = 5
b = 10

if a > 0:
    print('a is positive')
    if b > 0:
        print('b is positive')

print('########################################################')
print('# 논리연산자')

a = 1
b = 1

print(a == b)
print(a != b)
print(a < b)
print(a > 0 and b > 0)
print(a > 0 or b > 0)

print('########################################################')
print('# in, not')

y = [1, 2, 3]
x = 1

if x in y:
    print('in')
if 100 not in y:
    print('not in')

a = 1
b = 1

if not a == b:
    print('Not equal')
if a != b:
    print('Not equal')

print('########################################################')
print('# 값이 들어있지 않다는 판정을 하는 테크닉')

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

# Fasle, 0, 0.0, '', (), {}, set()

print('########################################################')
print('# None판정')
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

# is 는 Object자체를 비교


print('########################################################')
print('# while문, continue문, break문')

count = 0
while count < 5:
    print(count)
    count += 1

count = 0
while True:
    if count >= 5:
        break
    print(count)
    count += 1

print('########################################################')
print('# while else')

count = 0
while count < 5:
    print(count)
    count += 1
else:
    print('done')

# break가 없을 때, else를 실행하고 종료

count = 0
while count < 5:
    if count == 1:
        break
    print(count)
    count += 1
else:
    print('done')

print('########################################################')
print('# input 함수')

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
print('# for문, break문, continue문')

some_list = [10, 20, 30, 40, 50]

for i in some_list:
    print(i)

for word in ['My', 'name', 'is', 'Mike']:
    print(word)

for s in 'abcde':
    print(s)

print('########################################################')
print('# for else')

for fruit in ['apple', 'banana', 'orange']:
    print(fruit)
else:
    print('I ate all!')

for fruit in ['apple', 'banana', 'orange']:
    if fruit == 'banana':
        print('stop eating')
        break
    print(fruit)
else:
    print('I ate all!')

print('########################################################')
print('# range')

for i in range(10):
    print(i)

for i in range(2, 10):
    print(i)

for i in range(2, 10, 3):
    print(i)

for _ in range(10):
    print('hello')

print('########################################################')
print('# enumerate')

i = 0
for fruit in ['apple', 'banana', 'orange']:
    print(i, fruit)
    i += 1

for i, fruit in enumerate(['apple', 'banana', 'orange']):
    print(i, fruit)

print('########################################################')
print('# zip')

days = ['Mon', 'Tue', 'Wed']
fruits = ['apple', 'banan', 'orange']
drinks = ['coffee', 'tea', 'beer']

for i in range(len(days)):
    print(days[i], fruits[i], drinks[i])

for day, fruit, drink in zip(days, fruits, drinks):
    print(day, fruit, drink)

# len 다르면 에러 발생 IndexError: list index out of range

print('########################################################')
print('# 사전을 for문으로 처리하기')

d = {'x': 100, 'y': 200}
# key만
for v in d:
    print(v)

# key, value 둘다
for k, v in d.items():
    print(k, ':', v)

print(d.items())