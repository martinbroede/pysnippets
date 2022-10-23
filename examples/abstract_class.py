# Example usage of abc module which provides a concept for abstract classes respectively interfaces.
# Keywords:
# abstract class / abstract method / abc / interface / implements

from abc import ABC, abstractmethod


class Wakeable(ABC):

    @abstractmethod  # force subclasses to implement this method
    def wake_up(self):
        """Wakes up object."""


class Child(Wakeable):  # Child implements Wakeable - if you think of Wakeable as an interface.

    def wake_up(self):
        print("bäääh")


class NotWakeable(Wakeable):  # causes an IDE warning because abstract methods are not implemented
    pass


Child().wake_up()  # bäääh
NotWakeable()  # TypeError: Can't instantiate abstract class NotWakeable with abstract method wake_up

# Note that you can even use abc.abstractmethod without abc.ABC - if so, no TypeError will be raised when you
# instantiate NotWakeable, but you'll still get an IDE warning for not implementing abstract methods.
