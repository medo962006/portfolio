class Car:
    def __init__(self , color , mileage):
        self.color = color
        self.mileage = mileage
    def describe(self):
        print('The {} car has {} miles.'.format(self.color, self.mileage))
blue_car = Car('blue',30000)
red_car = Car('red' , 20000)
red_car.describe()
blue_car.describe()

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"


class Golden_Retriever(Dog):
    def bark(self):
        super().speak(sound='How How')