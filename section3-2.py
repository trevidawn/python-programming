print('########################################################')


# 함수 정의
# say_something() : error

def say_something():
    s = 'hi'
    return s


say_something()

f = say_something
print(type(f))

result = say_something()
print(result)


def what_is_this(color):
    if color == 'red':
        return 'tomato'
    elif color == 'green':
        return 'green pepper'
    else:
        return "I don't know"


result = what_is_this('red')
print(result)

print('########################################################')
# 함수의 인수와 반환값의 선언

num: int = 10


def add_num1(a, b):
    return a + b


def add_num2(a: int, b: int) -> int:
    return a + b


r = add_num2('a', 'b')
print(r)

print('########################################################')


# 위치 인수, 키워드 인수, 디폴트 인수

def menu(entree):
    print(entree)


menu('beef')


def menu2(entree, drink, dessert):
    print(entree)
    print(drink)
    print(dessert)


menu2('beef', dessert='ice', drink='beer')


def menu3(entree='beef', drink='wine', dessert='ice'):
    print(entree)
    print(drink)
    print(dessert)


menu3('chicken')

print('########################################################')


# 디폴트 인수를 쓸 때 주의할점

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


# Python에서 List는 디폴트 인수로 쓰면 안된다는 암묵적인 룰이있다. 그 외에도 참조 반황하는 자료형
# 리스트는 참조 반환,
# 함수선언에서 default 인수로 빈 리스트를 미리 만들어 놓음 -> 딱 한번만 생성이 된다.

def test_func2(x, l=None):
    if l is None:
        l = []
    l.append(x)
    return l


r = test_func2(123)
print(r)

print('########################################################')


# 위치 인수의 튜플화

def say_something(*args):
    print(args)


say_something('Hi!', 'Mike!', "nance")


def say_something2(word, *args):
    print(word)
    for arg in args:
        print(arg)


t = ('Mike', 'Nancy')
say_something('Hi!', *t)

print('########################################################')


# 키워드 인수의 사전화

def menu(entree='beef', drink='wine'):
    print(entree, drink)


menu(entree='beef', drink='coffee')


def menu2(**kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(k, v)


menu2(entree='aaa', d='aasd')

d = {
    'entree': 'beef',
    'drink': 'ice coffe',
    'dessert': 'ice'
}

menu2(**d)


def menu3(food, *args, **kwargs):
    print(food)
    print(args)
    print(kwargs)


menu3('banana', 'apple', 'orange', 'a', 'c', entree='beef', drink='coffee')

print('########################################################')


# Docstrings

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

print(example_func.__doc__)

print('########################################################')


# 함수 내 함수

def outer(a, b):
    def plus(c, d):
        return c + d

    r = plus(a, b)
    print(r)


outer(1, 2)

print('########################################################')


# 클로저


def outer(a, b):
    def inner():
        return a + b

    return inner


f = outer(1, 2)

r = f()
print(r)


def circle_area_func(pi):
    def circle_area(radius):
        return pi * radius * radius

    return circle_area


ca1 = circle_area_func(3.14)
ca2 = circle_area_func(3.141592)

print(ca1(10))
print(ca2(10))

print('########################################################')


# 데코레이터

def add_num(a, b):
    return a + b


print('start')
r = add_num(10, 20)
print('end')

print(r)


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


@print_info
def add_num2(a, b):
    return a + b


r = add_num2(33, 1233)
print(r)


def print_more(func):
    def wrapper(*args, **kwargs):
        print('func', func.__name__)
        print('args:', args)
        print('kwargs:', kwargs)
        result = func(*args, **kwargs)
        print('result:', result)
        return result

    return wrapper


print('%%%')


@print_info
@print_more
def add_num3(a, b):
    return a + b


r = add_num3(1, 2)
print(r)

print('########################################################')
# 람다

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
# 제너레이터
# iterator의 요소
# 반복적인 처리를 할 때 , 한 요소를 꺼내서 생성해나가는 역할

l = ['Good morning', 'Good afternoon', 'Good night']

for i in l:
    print(i)


def greeting():
    yield 'Good morning'
    yield 'Good afternoon '
    yield 'Good night'


for g in greeting():
    print(g)

g = greeting()
print(next(g))
print(next(g))


def counter(num=10):
    for _ in range(num):
        yield 'run'


c = counter(2)
print(next(c))
print(next(c))


def greeting2():
    yield 'Good morning'
    for i in range(3):
        print(i)
    yield 'Good afternoon '
    for i in range(3):
        print(i)
    yield 'Good night'


g2 = greeting2()
print(next(g2))
print(next(g2))

print('########################################################')
# 리스트 내포 표기

t = (1, 2, 3, 4, 5)

r = []
for i in t:
    r.append(i)

print(r)

r = [i for i in t]
print(r)
r = [i for i in t if i % 2 == 0]
print(r)

t2 = (5, 6, 7, 8, 9, 10)
r = [i * j for i in t for j in t2]
print(r)

print('########################################################')
# 사전의 내포 표기
w = ['mon', 'tue', 'wed']
f = ['coffee', 'milk', 'water']

d = {}

for x, y in zip(w, f):
    d[x] = y

print(d)

d = {x: y for x, y in zip(w, f)}
print(d)

print('########################################################')
# 집합 내포 표기

s = set()

for i in range(10):
    s.add(i)

print(s)

s = {i for i in range(10) if i % 2 == 0}
print(s)

print('########################################################')


# 제너레이터 내포 표기

def g():
    for i in range(10):
        yield i


g = g()

g = (i for i in range(10))
print(type(g))
print(next(g))

g2 = tuple(i for i in range(10))
print(type(g2))
print(g2)

g3 = (i for i in range(10) if i % 2 == 0)

for x in g3:
    print(x)

print('########################################################')
# 이름공간과 스코프

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

print('########################################################')
# 에러 핸들링

l = [1, 2, 3]
i = 5

try:
    l[0]
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


# 독자 예외의 작성

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

