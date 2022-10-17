# Example usage of magic method __new__.
# Keywords:
# new / constructor / singleton pattern / factory method / class constructor


class Singleton:
    __instance = None

    def __new__(cls):
        if cls.__instance:
            return cls.__instance
        else:
            cls.__instance = super().__new__(cls)
            return cls.__instance


class Usual:
    pass


one = Singleton()
another = Singleton()
print(f"surprise, surprise! one is another == {one is another}")  # True

one = Usual()
another = Usual()
print(f"usual behaviour: one is another == {one is another}")  # False
