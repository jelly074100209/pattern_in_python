class Dog(object):
    def __init__(self):
        self.name = "Dog"

    def bark(self):
        return "woof!"


class Cat(object):
    def __init__(self):
        self.name = "Cat"

    def meow(self):
        return "meow!"


class Human(object):
    def __init__(self):
        self.name = "Human"

    def speak(self):
        return "Hello"


class Car(object):
    def __init__(self):
        self.name = "Car"

    def make_noise(self, octane_level):
        return "vroom%s" % ("!" * octane_level)


class Adapter(object):
    """
    Adapter an object replacing methods.
    Usage:
    dog = Dog
    dog = Adapter(dog, dict(make_noise=dog.bark)
    """

    def __init__(self, obj, adapted_methods):
        """We set the adapted methods in the object's dict"""
        self.obj = obj
        self.__dict__.update(adapted_methods)

    pass


def main():
    objects = []
    dog = Dog()
    cat = Cat()
    human = Human()
    objects.append(Adapter(dog, dict(make_noise=dog.bark)))
    objects.append(Adapter(cat, dict(make_noise=cat.meow)))
    objects.append(Adapter(human, dict(make_noise=human.speak)))

    car = Car()
    car_noise = lambda : car.make_noise(3)
    objects.append(Adapter(car, dict(make_noise=car_noise)))

    for obj in objects:
        print("A ", obj.name, " goes ", obj.make_noise())


if __name__ == "__main__":
    main()
