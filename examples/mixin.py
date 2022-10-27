# Building and usage of mixins.
# Keywords:
# multiple inheritance / mixin

class Readable:
    """Mixin for printing objects in a structured, human-readable way."""

    def __str__(self):  # Magic method that provides a string representation which focuses on readability
        info = [self.__class__.__name__] + [f"{str(attr)}: {str(val)}" for (attr, val) in self.__dict__.items()]
        return "\n".join(info)


class Unfoldable:
    """Mixin that lets you create and assign instance attributes via keyword arguments."""

    def __new__(cls, *args, **kwargs):
        obj = object().__new__(cls)
        for key, value in kwargs.items():
            obj.__setattr__(key, value)
        return obj


class Subscriptable:
    """Mixin that simulates javascript-like access to object attributes."""

    def __getitem__(self, item):  # Magic method that makes your class subscriptable, i.e. you can access items via [].
        return self.__getattribute__(item)

    def __setitem__(self, key, value):  # Magic method that lets you assign values to subscripted items.
        self.__setattr__(key, value)


class Data(Readable, Unfoldable, Subscriptable):
    pass


data = Data(name="jane doe", age=42, job="developer")  # 'Data' is 'Unfoldable' so you can assign instance variables
# directly through keyword arguments

data['age'] = 24  # You can access the age attribute since 'Data' is 'Subscriptable'.

print(data)  # You get a readable representation since 'Data' is 'Readable'.
# Data
# name: jane doe
# age: 24
# job: developer
