print('########################################################')


# 클래스의 정의

class Person(object):
    def say_something(self):
        print('hello')


# object쓰면 계승이라는 것을 말할 때, base class로 쓸 수 있기 때문에 object라고 써도 된다.

person = Person()
person.say_something()

print('########################################################')


# 클래스의 초기화와 클래스 변수

class Person2:
    def __init__(self, name):
        self.name = name

    def say_something(self):
        print('I am {}. hello'.format(self.name))
        self.run(2)

    def run(self, num):
        print('run' * num)


person2 = Person2('Mike')
person2.say_something()

print('########################################################')


# 생성자와 소멸자

class Person3:
    def __init__(self, name):
        self.name = name

    def say_something(self):
        print('I am {}. hello'.format(self.name))
        self.run(2)

    def run(self, num):
        print('run' * num)

    def __del__(self):
        print('good bye')


person3 = Person3('Mike')
person3.say_something()

del person3

print('########################################################')


# 클래스의 계승


class Car(object):
    def __init__(self, model=None):
        self.model = model

    def run(self):
        print('run')


class ToyotaCar(Car):
    pass


car = Car()
car.run()

toyota_car = ToyotaCar('Lexus')
print(toyota_car.model)
toyota_car.run()


class TeslaCar(Car):
    def __init__(self, model='Model S',
                 enable_auto_run=False,
                 passwd='123'):
        super().__init__(model)
        self._enable_auto_run = enable_auto_run
        self.passwd = passwd

    @property
    def enable_auto_run(self):
        return self._enable_auto_run

    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):
        if self.passwd == '123':
            self._enable_auto_run = is_enable
        else:
            raise ValueError

    def run(self):
        print('super fast')

    def auto_run(self):
        print('auto run')


tesla_car = TeslaCar()
print(tesla_car.model)
print(type(tesla_car.model))
tesla_car.run()
tesla_car.auto_run()

tesla_car.enable_auto_run = True
print(tesla_car.enable_auto_run)

# __ 두개 붙이면 private -> 외부에서 접근 안됨, 내부는 가능
# _ 하나는 안보이기만 하고 외부에서 접근은 가능

print('########################################################')


# 클래스를 구조체로서 쓸 때의 주의점

class T:
    pass


t = T()
t.name = 'Mike'
t.age = 20
print(t.name, t.age)

tesla_car.__enable_auto_run = 'XX'
print(tesla_car.__enable_auto_run)  # 에러 안남 나옴, 덮어씀 그래서 class밖에서 멤버변수 만들어서 덮어씌우는거 잘 안쓰지만, 주의해야함

print('########################################################')


# 덕타이핑

class Person:
    def __init__(self, age=1):
        self.age = age

    def drive(self):
        if self.age >= 18:
            print('ok')
        else:
            raise Exception('No drive')


class Baby(Person):
    def __init__(self, age=1):
        if age < 18:
            super().__init__(age)
        else:
            raise ValueError


class Adult(Person):
    def __init__(self, age=18):
        if age >= 18:
            super().__init__(age)
        else:
            raise ValueError


baby = Baby()
adult = Adult()


class Car:
    def __init__(self, model=None):
        self.model = model

    def run(self):
        print('run')

    def ride(self, person):
        person.drive()


car = Car()
car.ride(adult)
# car.ride(baby)

print('########################################################')
# 추상 클래스, 뭐 안써도 된다는 의견도 있다. 팀바팀, 컨벤션

import abc


class Person(metaclass=abc.ABCMeta):
    def __init__(self, age=1):
        self.age = age

    @abc.abstractmethod
    def drive(self):
        pass


class Baby(Person):
    def __init__(self, age=1):
        if age < 18:
            super().__init__(age)
        else:
            raise ValueError

    def drive(self):
        raise Exception('No drive')


class Adult(Person):
    def __init__(self, age=18):
        if age >= 18:
            super().__init__(age)
        else:
            raise ValueError

    def drive(self):
        print('ok')


baby = Baby()
adult = Adult()


class Car:
    def __init__(self, model=None):
        self.model = model

    def run(self):
        print('run')

    def ride(self, person):
        person.drive()


car = Car()
car.ride(adult)
# car.ride(baby)

print('########################################################')


# 다중 계승

class Person:
    def talk(self):
        print('talk')

    def run(self):
        print('person run')


class Car:
    def run(self):
        print('run')


class PersonCarRobot(Person, Car):
    def fly(self):
        print('fly')


person_car_robot = PersonCarRobot()
person_car_robot.talk()
person_car_robot.run()  # 왼쪽에 먼저 있는게 실행됨
person_car_robot.fly()

print('########################################################')


# 클래스 변수

class Person:
    def __init__(self, name):
        self.kind = 'human'
        self.name = name

    def who_are_you(self):
        print(self.name, self.kind)


a = Person('A')
a.who_are_you()
b = Person('B')
b.who_are_you()


class Person:
    kind = 'human'  # 모든 인스턴스에서 공유됨 static같네

    def __init__(self, name):
        self.name = name

    def who_are_you(self):
        print(self.name, self.kind)


a = Person('A')
a.who_are_you()
b = Person('B')
b.who_are_you()


class T:
    words = []

    def add_word(self, word):
        self.words.append(word)


c = T()
c.add_word('add 1')
c.add_word('add 2')
print(c.words)

d = T()
d.add_word("add 3")
d.add_word("add 4")
print(d.words)

print('########################################################')


# 클래스 메서드와 스태틱 메서드

class Person:
    kind = 'human'

    def __init__(self):
        self.x = 100

    @classmethod
    def what_is_your_kind(cls):
        return cls.kind

    @staticmethod
    def about():
        print('about human')


a = Person()
print(a)  # instance
print(a.what_is_your_kind())

b = Person
print(b)  # class
print(b.kind)
print(b.what_is_your_kind())

print(Person.what_is_your_kind())
Person.about()

print('########################################################')


# 특수 메서드

class Word:

    def __init__(self, text):
        self.text = text

    def __str__(self):
        return 'Word!!!!'

    def __len__(self):
        return len(self.text)

    def __add__(self, word):
        return self.text.lower() + word.text.lower()

    def __eq__(self, word):
        return self.text.lower() == word.text.lower()

w = Word('test')
print(w)
print(len(w))

w2 = Word('#@$')

print(w + w2)
print(w == w2)

# __eq__ 없는 상태에서는 word.text같아도 False로 나옴, 서로 다른 인스턴스이기 때문

