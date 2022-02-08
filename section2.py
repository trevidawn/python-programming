print('########################################################')
print('리스트')
print('########################################################')

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
print()
"""OUTPUT
1
20
2
1
[1, 20]
[1, 20, 4, 50, 2, 1, 2]
[1, 20, 4, 50, 2, 1, 2]
7
<class 'list'>
['b', 'c', 'd', 'e', 'd', 'i', 't']
"""

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(n[::2])
print(n[::-1])
print(n[::3])
print(n[::100])
print()
"""OUTPUT
[1, 3, 5, 7, 9]
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
[1, 4, 7, 10]
[1]
"""

a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
print(x[0])
print(x[1])
print(x[0][1])
print()
"""OUTPUT
[['a', 'b', 'c'], [1, 2, 3]]
['a', 'b', 'c']
[1, 2, 3]
b
"""

print('########################################################')
print('리스트의 조작')
print('########################################################')

s = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
s[0] = 'X'
print(s)
print()
"""OUTPUT
['X', 'b', 'c', 'd', 'e', 'f', 'g']
"""

s[2:5] = ['C', 'D', 'E']
print(s)
print()
"""OUTPUT
['X', 'b', 'C', 'D', 'E', 'f', 'g']
"""

s[:] = []
print(s)
print()
"""OUTPUT
[]
"""

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n.append(100)
print(n)
print()
"""OUTPUT
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100]
"""

n.insert(0, 200)
print(n)
print()
"""OUTPUT
[200, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100]
"""

n.pop()
print(n)
print()
"""OUTPUT
[200, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""

n.pop(0)
print(n)
print()
"""OUTPUT
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""

del n[0]  # 주의해서 써야함
print(n)
print()
"""OUTPUT
[2, 3, 4, 5, 6, 7, 8, 9, 10]
"""

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
print()
"""OUTPUT
[1, 2, 2, 3]
[1, 2, 3]
[1, 3]
[1, 3]
"""

# list 결함
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
x = a + b
print(x)
print()
"""OUTPUT
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""

x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 10]
x.extend(y)
print(x)
print()
"""OUTPUT
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""

print('########################################################')
print('리스트의 메서드')
print('########################################################')

r = [1, 2, 3, 4, 5, 1, 2, 3]
print(r.index(3))
print(r.index(3, 3))  # 첫번째 인자의 인덱스부터  3을 겁색
print(r.count(3))
if 5 in r:
    print('exist')
print()
"""OUTPUT
2
7
2
exist
"""

r.sort()
print(r)
r.sort(reverse=True)
print(r)
r.reverse()
print(r)
print()
"""OUTPUT
[1, 1, 2, 2, 3, 3, 4, 5]
[5, 4, 3, 3, 2, 2, 1, 1]
[1, 1, 2, 2, 3, 3, 4, 5]
"""

s = 'My name is Mike.'
to_split = s.split(' ')
print(to_split)

x = ' '.join(to_split)
print(x)
y = '##'.join(to_split)
print(y)
print()
"""OUTPUT
['My', 'name', 'is', 'Mike.']
My name is Mike.
My##name##is##Mike.
"""

print('########################################################')
print('리스트의 복사')
print('########################################################')

i = [1, 2, 3, 4, 5]
j = i
j[0] = 100
print('j =', j)
print('i =', i)
print()
"""OUTPUT
j = [100, 2, 3, 4, 5]
i = [100, 2, 3, 4, 5]
"""

x = [1, 2, 3, 4, 5]
y = x.copy()
y[0] = 100
print('x =', x)
print('y =', y)
print()
"""OUTPUT
x = [1, 2, 3, 4, 5]
y = [100, 2, 3, 4, 5]
"""

y2 = x[:]
y2[0] = 100
print('x =', x)
print('y2 =', y2)
print()
"""OUTPUT
x = [1, 2, 3, 4, 5]
y2 = [100, 2, 3, 4, 5]
"""

print('########################################################')
print('튜플형')
print('########################################################')

t = (1, 2, 3, 4, 1, 2)
# t[0] = 100 TypeError: 'tuple' object does not support item asignment
print(t[0])
print(t[-1])
print(t[2:5])
print(t.index(1))
print(t.index(1, 1))
print(t.count(1))
print()
"""OUTPUT
1
2
(3, 4, 1)
0
4
2
"""


t = ([1, 2, 3], [4, 5, 6])
print(t)
# t[0] = [2] : TypeError: 'tuple' object does not support item assignment
t[0][0] = 3
print(t)
print()
"""OUTPUT
([1, 2, 3], [4, 5, 6])
([3, 2, 3], [4, 5, 6])
"""

print('########################################################')
print('튜플의 언패킹')
print('########################################################')

num_tuple = (10, 20)
x, y = num_tuple
print(x, y)

x, y = 10, 20  # 자동으로 Tuple로 인식
print(x, y)
print()
"""OUTPUT
10 20
10 20
"""

a = 100
b = 200
a, b = b, a
print(a, b)
print()
"""OUTPUT
200 100
"""

print('########################################################')
print('사전형')
print('########################################################')

d = {'x': 10, 'y': 20}
print(d['x'])
print(d['y'])
d['x'] = '100'
print(d['x'])
d['z'] = 200
print(d)
d[1] = 10000
print(d)
print()
"""OUTPUT
10
20
100
{'x': '100', 'y': 20, 'z': 200}
{'x': '100', 'y': 20, 'z': 200, 1: 10000}
"""

print(dict(a=10, b=20))
print(dict([('a', 10), ('b', 20)]))
print()
"""OUTPUT
{'a': 10, 'b': 20}
{'a': 10, 'b': 20}
"""

print('########################################################')
print('사전형의 메서드')
print('########################################################')

d = {'x': 10, 'y': 20}
print(d.keys())
print(d.values())
print()
"""OUTPUT
dict_keys(['x', 'y', 'z', 1])
dict_values(['100', 20, 200, 10000])
"""

d2 = {'x': 1000, 'j': 500}
d.update(d2)
print(d)  # x는 1000으로 update , j 는 추가
r = d.get('zzz')
print(r)
print(type(r))
print()
"""OUTPUT
{'x': 1000, 'y': 20, 'j': 500}
None
<class 'NoneType'>
"""

d.pop('x')
print(d)
del d['y']
print(d)
d.clear()
print(d)
print('a' in d)
print()
"""OUTPUT
{'y': 20, 'j': 500}
{'j': 500}
{}
False
"""


print('########################################################')
print('사전형의 복사')
print('########################################################')

x = {'a': 1}
y = x
y['a'] = 1000
print(x)
print(y)
print()
"""OUTPUT
{'a': 1000}
{'a': 1000}
"""


x = {'a': 1}
y = x.copy()
y['a'] = 100
print(x)
print(y)
print()
"""OUTPUT
{'a': 1}
{'a': 100}
"""

print('########################################################')
print('집합형')
print('########################################################')

a = {1, 2, 2, 3, 4, 4, 4, 5, 6}
b = {2, 3, 3, 5, 6, 7}
print(a - b)
print(b - a)
print(a & b)
print(a | b)
print(a ^ b)
print()
"""OUTPUT
{1, 4}
{7}
{2, 3, 5, 6}
{1, 2, 3, 4, 5, 6, 7}
{1, 4, 7}
"""

print('########################################################')
print('# 집합형의 메서드')

s = {1, 2, 3, 4, 5}
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
print()
"""OUTPUT
{1, 2, 3, 4, 5, 6}
{1, 2, 3, 4, 5, 6}
{1, 2, 3, 4, 5}
set()
False
"""

f = ['apple', 'banana', 'apple', 'banana']
kind = set(f)
print(kind)
print()
"""OUTPUT
{'apple', 'banana'}
"""
