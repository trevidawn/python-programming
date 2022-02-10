print('########################################################')
print('# 함수 정의')
print('########################################################')


def say_something():
    s = 'hi'
    return s


f = say_something
print(type(f))

result = say_something()
print(result)
print()
"""OUTPUT
<class 'function'>
hi
"""

print('########################################################')
print('# 함수의 인수와 반환값의 선언')
print('########################################################')


def add_num1(a, b):
    return a + b


def add_num2(a: int, b: int) -> int:
    return a + b


r = add_num2('a', 'b')
print(r)
print()
"""OUTPUT
ab
"""

print('########################################################')
print('# 위치 인수, 키워드 인수, 디폴트 인수')
print('########################################################')


def menu2(entree, drink, dessert):
    print(entree)
    print(drink)
    print(dessert)


menu2('beef', dessert='ice', drink='beer')
print()


def menu3(entree='beef', drink='wine', dessert='ice'):
    print(entree)
    print(drink)
    print(dessert)


menu3('chicken')
print()
"""OUTPUT
beef
beer
ice

chicken
wine
ice
"""

print('########################################################')
print('# 디폴트 인수를 쓸 때 주의할점')
print('########################################################')


def test_func(x, l=[]):
    l.append(x)
    return l


y = [1, 2, 3]
r = test_func(100, y)
print(r)

r = test_func(100)
print(r)

r = test_func(100)
print(r)
print()
"""OUTPUT
[1, 2, 3, 100]
[100]
[100, 100]

# Python에서 List는 디폴트 인수로 쓰면 안된다는 암묵적인 룰이있다. 그 외에도 참조 반황하는 자료형
# 리스트는 참조 반환,
# 함수선언에서 default 인수로 빈 리스트를 미리 만들어 놓음 -> 딱 한번만 생성이 된다.
"""


def test_func2(x, l=None):
    if l is None:
        l = []
    l.append(x)
    return l


r = test_func2(123)
print(r)
print()
"""OUTPUT
[123]
"""

print('########################################################')
print('# 위치 인수의 튜플화')
print('########################################################')


def say_something(*args):
    print(args)


say_something('Hi!', 'Mike!', "nance")
print()


def say_something2(word, *args):
    print(word)
    for arg in args:
        print(arg)


t = ('Mike', 'Nancy')
say_something('Hi!', *t)
print()
"""OUTPUT
('Hi!', 'Mike!', 'nance')

('Hi!', 'Mike', 'Nancy')
"""

print('########################################################')
print('"# 키워드 인수의 사전화')
print('########################################################')


def menu(entree='beef', drink='wine'):
    print(entree, drink)


menu(entree='beef', drink='coffee')
print()


def menu2(**kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(k, v)


menu2(entree='aaa', d='aasd')
print()

d = {
    'entree': 'beef',
    'drink': 'ice coffe',
    'dessert': 'ice'
}

menu2(**d)
print()
"""OUTPUT
beef coffee

{'entree': 'aaa', 'd': 'aasd'}
entree aaa
d aasd

{'entree': 'beef', 'drink': 'ice coffe', 'dessert': 'ice'}
entree beef
drink ice coffe
dessert ice
"""


def menu3(food, *args, **kwargs):
    print(food)
    print(args)
    print(kwargs)


menu3('banana', 'apple', 'orange', 'a', 'c', entree='beef', drink='coffee')
print()
"""OUTPUT
banana
('apple', 'orange', 'a', 'c')
{'entree': 'beef', 'drink': 'coffee'}
"""

print('########################################################')
print('# Docstrings')
print('########################################################')


def example_func(param1, param2):
    """

    Args:
        :param param1:
        :param param2:

    Retruns:
        :return:
    """
    print(param1)
    print(param2)
    return True


help(example_func)

print('########################################################')
print('# 함수 내 함수')
print('########################################################')


def outer(a, b):
    def plus(c, d):
        return c + d

    r = plus(a, b)
    print(r)


outer(1, 2)
"""OUTPUT
3
"""

print('########################################################')
print('# 클로저')
print('########################################################')


def outer(a, b):
    def inner():
        return a + b

    return inner


f = outer(1, 2)

r = f()
print(r)
print(r)
print()
"""OUTPUT
3
3
"""


def circle_area_func(pi):
    def circle_area(radius):
        return pi * radius * radius

    return circle_area


ca1 = circle_area_func(3.14)
ca2 = circle_area_func(3.141592)

print(ca1(10))
print(ca2(10))
print()
"""OUTPUT
314.0
314.1592
"""

print('########################################################')
print('# 데코레이터')
print('########################################################')


def add_num(a, b):
    return a + b


def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result

    return wrapper


f = print_info(add_num)
r = f(11, 22)
print(r)
print()
"""OUTPUT
start
end
33
"""


@print_info
def add_num2(a, b):
    return a + b


r = add_num2(33, 1233)
print(r)
print()
"""OUTPUT
start
end
1266
"""


def print_more(func):
    def wrapper(*args, **kwargs):
        print('func', func.__name__)
        print('args:', args)
        print('kwargs:', kwargs)
        result = func(*args, **kwargs)
        print('result:', result)
        return result

    return wrapper


@print_info
@print_more
def add_num3(a, b):
    return a + b


r = add_num3(1, 2)
print(r)
print()
"""OUTPUT
start
func add_num3
args: (1, 2)
kwargs: {}
result: 3
end
3
"""

print('########################################################')
print('# 람다')
print('########################################################')

l = ['Mon', 'tue', 'Wed', 'Thu', 'fri', 'sat', 'Sun']


def change_words(words, func):
    for word in words:
        print(func(word))


def sample_func(word):
    return word.capitalize()


change_words(l, sample_func)

# apply lambda

sample_func2 = lambda word: word.capitalize()

change_words(l, sample_func2)
change_words(l, lambda word: word.capitalize())

print('########################################################')
print('# 제너레이터')
print('# iterator의 요소')
print('# 반복적인 처리를 할 때 , 한 요소를 꺼내서 생성해나가는 역할')
print('########################################################')


def greeting():
    yield 'Good morning'
    yield 'Good afternoon '
    yield 'Good night'


for g in greeting():
    print(g)
print()
"""OUTPUT
Good morning
Good afternoon 
Good night
"""

g = greeting()
print(next(g))
print(next(g))
print()
"""OUTPUT
Good morning
Good afternoon 
"""


def counter(num=10):
    for _ in range(num):
        yield 'run'


c = counter(2)
print(next(c))
print(next(c))
print()
"""OUTPUT
run
run
"""


def greeting2():
    yield 'Good morning'

    for i in range(1):
        print(i)
    yield 'Good afternoon '

    for i in range(1):
        print(i)
    yield 'Good night'


g2 = greeting2()
print(next(g2))
print()
print(next(g2))
print()
print(next(g2))
print()
"""OUTPUT
Good morning

0
Good afternoon 

0
Good night 
"""

print('########################################################')
print('# 리스트 내포 표기')
print('########################################################')

t = (1, 2, 3, 4, 5)

r = [i for i in t]
print(r)
r = [i for i in t if i % 2 == 0]
print(r)
print()
"""OUTPUT

"""

t2 = (5, 6, 7, 8, 9, 10)
r = [i * j for i in t for j in t2]
print(r)
print()
"""OUTPUT
[1, 2, 3, 4, 5]
[2, 4]

[5, 6, 7, 8, 9, 10, 10, 12, 14, 16, 18, 20, 15, 18, 21, 24, 27, 30, 20, 24, 28, 32, 36, 40, 25, 30, 35, 40, 45, 50]
"""

print('########################################################')
print('# 사전의 내포 표기')
print('########################################################')
w = ['mon', 'tue', 'wed']
f = ['coffee', 'milk', 'water']

dict = {x: y for x, y in zip(w, f)}
print(dict)
print()
"""OUTPUT
{'mon': 'coffee', 'tue': 'milk', 'wed': 'water'}
"""

print('########################################################')
print('"# 집합 내포 표기')
print('########################################################')

s = set()
for i in range(10):
    s.add(i)
print(s)
print()
"""OUTPUT
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
"""

s = {i for i in range(10) if i % 2 == 0}
print(s)
print()
"""OUTPUT
{0, 2, 4, 6, 8}
"""

print('########################################################')
print('# 제너레이터 내포 표기')
print('########################################################')


def g():
    for i in range(10):
        yield i


g = g()
print(type(g))
print(next(g))
print()

g = (i for i in range(10))
print(type(g))
print(next(g))
print()

g2 = tuple(i for i in range(10))
print(type(g2))
print(g2)
print()

g3 = (i for i in range(10) if i % 2 == 0)
print(type(g3))
print(next(g3))
print(next(g3))
print()
"""OUTPUT
<class 'generator'>
0

<class 'generator'>
0

<class 'tuple'>
(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

<class 'generator'>
0
2
"""

print('########################################################')
print('# 이름공간과 스코프')
print('########################################################')

animal = 'cat'
print(animal)


def f():
    # print(animal)
    animal = 'dog'
    print('after', animal)


f()


def f2():
    global animal
    animal = 'dog'
    print('local', animal)


f2()
print('global:', animal)
"""OUTPUT
cat
after dog
local dog
global: dog
"""

print('########################################################')
print('# 에러 핸들링')
print('########################################################')

l = [1, 2, 3]
i = 5

try:
    l[12]
except IndexError as ex:
    print("Don't worry: {}".format(ex))
except NameError as ex:
    print(ex)
except Exception as ex:
    print('other:{}'.format(ex))
else:
    print('done')
finally:
    print('clean up')

# Exception hierarchy - Python document

print('########################################################')
print('# 독자 예외의 작성')
print('########################################################')


# 예외 발생
# raise IndexError('test error')

class UppercaseError(Exception):
    pass


def check():
    words = ['APPLE', 'orange', 'banana']
    for word in words:
        if word.isupper():
            raise UppercaseError(word)


try:
    check()
except UppercaseError as exc:
    print('This is my fault. Go next')

"""OUTPUT
This is my fault. Go next
"""