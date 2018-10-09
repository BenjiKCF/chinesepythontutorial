class Animal(object):
    def run(self):
        print('Animal is running...')

def run_twice(a): # anything is an animal class can run
    a.run()
    a.run()

class Dog(Animal):

    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')


class Cat(Animal):

    def run(self):
        print('Cat is running...')

class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')

dog = Dog()
dog.run()

cat = Cat()
cat.run()

run_twice(Tortoise())
