from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def doAction(self):
        pass

    @property
    @abstractmethod
    def gender(self):
        pass


class Human(Animal):
    def __init__(self, gender):
        print('I Can walk and run')
        self.__gender = gender

    def doAction(self):
        print('i Can walk')

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, value):
        self.__gender = value


# akhil = Human('male')
# akhil.gender = 'female'
# print(akhil.gender)


# s = set()
# s.add('sjghv')
# s.add('sjghv1243')
# print(s)
# my_int = 10
#
# print(my_int)
# print(id(my_int))
# my_int = 30
#
# print(my_int)
# print(id(my_int))
#
# def printinfo(arg1, *vartuple):
#     "This prints a variable passed arguments"
#     print("Output is: ")
#     print(arg1)
#     for var in vartuple:
#         print(var)
#     return;
#
#
# # # Now you can call printinfo function
# # printinfo(10)
# # printinfo(70, 60, 50)
# s1={1,2,3,4,5}
# s2={4,5,6,7,8}
# s3 = {*s1, *s2}
# print (s3)


class division:
    def __init__(self, a, b):
        self.n = a
        self.d = b

    def divide(self):
        return self.n / self.d


class modulus:
    def __init__(self, a, b):
        self.n = a
        self.d = b

    def mod_divide(self):
        return self.n % self.d


class div_mod(division, modulus):
    def __init__(self, a, b, c):
        self.n = a
        self.d = b
        self.e = c

    def div_mod(self):
        div_val = division.divide(self)
        mod_val = modulus.mod_divide(self)
        return div_val, mod_val


# x = div_mod(10, 3, 8)
# print(x.divide())
# print(x.mod_divide())
# print(x.div_mod())


class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print('hello', self.name)


class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def greet(self):
        # Parent.greet(self)
        super().greet()
        print('i am', self.age)


c = Child('Akhil', 10)


# c.greet()
#
# class example:
#     def add(self, a, b):
#         x = a + b
#         return x
#
#     def add(self, a, b, c):
#         x = a + b + c
#         return x
#
#
# obj = example()
#
# print(obj.add(10, 20, 30))
# print(obj.add(10, 20))


# class SingletonClass:
#     _instance = None
#
#     def __new__(cls):
#         if cls._instance is None:
#             print('Creating the object')
#             cls._instance = super(SingletonClass,cls)
#         return cls._instance
#


def decorator_function(Wrapped):
    class Wrapper:
        def __init__(self, x):
            self.wrap = Wrapped(x)

        def print_name(self):
            return self.wrap.name

    return Wrapper


@decorator_function
class Wrapped:
    def __init__(self, x):
        self.name = x


#
# obj = Wrapped('Tutorials')
# print(obj.print_name())


from math import *
from collections import *
from sys import *
from os import *


## Read input as specified in the question.
## Print output as specified in the question.
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1

    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(1))
