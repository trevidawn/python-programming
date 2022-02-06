print('########################################################')
print('# 1. 리스트')

l = [1, 20, 4, 50, 2, 1, 2]
print(l[0])
print(l[1])
print(l[-1])
print(l[-2])
print(l[:2])
print(l[:])
print(l)
print(len(l))
print(type(l))
print(list('bcdedit'))

# print(l[100]) // index error

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(n[::2])
print(n[::-1])
print(n[::3])
print(n[::100])

a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
print(x[0])
print(x[1])
print(x[0][1])

print('########################################################')
print('# 2. 리스트의 조작')

s = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(s)
print(s[0])
s[0] = 'X'
print(s[0])

s[2:5] = ['C', 'D', 'E']
print(s)

s[:] = []
print(s)

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n.append(100)
print(n)

n.insert(0, 200)
print(n)

n.pop()
print(n)

n.pop(0)
print(n)

del n[0]  # 주의해서 써야함
print(n)

del n  # n 자체 삭제
# print(n) :: NameError: name 'n' is not defined

n = [1, 2, 2, 2, 3]
n.remove(2)  # 제일 처음의 2를 지움
print(n)
n.remove(2)
print(n)
n.remove(2)
print(n)
# n.remove(2) Error:: ValueError: list.remove(x): x not in list
print(n)

# list 결함
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

x = a + b

print(x)

a += b
print(a)

x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 10]
x.extend(y)
print(x)
print('########################################################')
print('# 3. 리스트의 메서드')

r = [1, 2, 3, 4, 5, 1, 2, 3]
print(r.index(3))
print(r.index(3, 3))  # 첫번째 인덱스부터  3을 겁색

print(r.count(3))

if 5 in r:
    print('exist')

r.sort()
print(r)
r.sort(reverse=True)
print(r)
r.reverse()
print(r)
s = 'My name is Mike.'
to_split = s.split(' ')
print(to_split)

x = ' '.join(to_split)
print(x)
y = '##'.join(to_split)
print(y)

print('########################################################')
print('# 4. 리스트의 복사')

i = [1, 2, 3, 4, 5]
j = i
j[0] = 100

print('j =', j)
print('i =', i)

x = [1, 2, 3, 4, 5]
y = x.copy()
y[0] = 100
print('x =', x)
print('y =', y)

y2 = x[:]
y2[0] = 100
print('x =', x)
print('y2 =', y2)

print('########################################################')
print('# 6. 튜플형')

t = (1, 2, 3, 4, 1, 2)
print(t)
print(type(t))

# t[0] = 100 TypeError: 'tuple' object does not support item asignment
print(t[0])
print(t[-1])
print(t[2:5])
print(t.index(1))
print(t.index(1, 1))
print(t.count(1))

t = ([1, 2, 3], [4, 5, 6])
print(t)

t[0][0] = 3
print(t)

print('########################################################')
print('# 튜플의 언패킹')

num_tuple = (10, 20)
print(num_tuple)

x, y = num_tuple
print(x, y)

x, y = 10, 20  # 자동으로 Tuple로 인식
print(x, t)

a, b, c, d, e, f = 'Mike', '1', '1', '1', 'e', 'f'
print(a, b, c, d, e, f)

i = 10
j = 20
tmp = i
i = j
j = tmp
print(i, j)

a = 100
b = 200

a, b = b, a
print(a, b)

print('########################################################')
print('# 사전형')

d = {'x': 10, 'y': 20}
print(type(d))
print(d['x'])
print(d['y'])
d['x'] = '100'
print(d['x'])
d['z'] = 200
print(d)

d[1] = 10000
print(d)

print(dict(a=10, b=20))
print(dict([('a', 10), ('b', 20)]))

print('########################################################')
print('# 사전형의 메서드')

print(d.keys())
print(d.values())

d2 = {'x': 1000, 'j': 500}
d.update(d2)
print(d)  # x는 1000으로 update , j 는 추가
print(d.get('x'))
r = d.get('zzz')
print(r)
print(type(r))

d.pop('x')
print(d)

del d['y']
print(d)

d.clear()
print(d)

print('a' in d)

print('########################################################')
print('# 사전형의 복사')

x = {'a': 1}
y = x
y['a'] = 1000
print(x)
print(y)

x = {'a': 1}
y = x.copy()
y['a'] = 100

print(x)
print(y)

print('########################################################')
print('# 집합형')

a = {1, 2, 2, 3, 4, 4, 4, 5, 6}
print(a)
print(type(a))
b = {2, 3, 3, 5, 6, 7}
print(b)
print(a - b)
print(b - a)
print(a & b)
print(a | b)
print(a ^ b)

print('########################################################')
print('# 집합형의 메서드')

s = {1, 2, 3, 4, 5}
print(s)
# print(s[0]) TypeError: 'set' object is not subscriptable

s.add(6)
print(s)
s.add(6)
print(s)
s.remove(6)
print(s)

s.clear()
print(s)

print(1 in s)

f = ['apple', 'banana', 'apple', 'banana']
kind = set(f)
print(kind)
