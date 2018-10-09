# -*- coding: utf-8 -*-
# Mixin = 2 class, class Dog(Mammal, Runnable):

class Animal(object):
    pass

class RunnableMixin(object):
    def run(self):
        print('Running...')

class FlyableMixin(object):
    def fly(self):
        print('Flying...')

class CarnivorousMixin(object):
    def eat(self):
        print('Fresh meat')

class HerbivoresMixin(object):
    def eat(self):
        print('Fresh grass')

# 大類:
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

# 各種動物:
class Dog(Mammal, RunnableMixin, CarnivorousMixin):
    pass

class Bat(Mammal, FlyableMixin, CarnivorousMixin):
    pass

class Parrot(Bird, FlyableMixin, HerbivoresMixin):
    pass

class Ostrich(Bird, RunnableMixin, HerbivoresMixin):
    pass
