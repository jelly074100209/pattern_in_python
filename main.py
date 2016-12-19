# main file

print("Hello World")


class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            origin = super(Singleton, cls)
            cls._instance = origin.__new__(cls, *args, **kw)
        return cls._instance


class MyClass(Singleton):
    a = 1


one = MyClass()
two = MyClass()

two.a = 3
print(one.a)
