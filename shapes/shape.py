from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def get_size_info(self):
        pass

    def __str__(self):
        pass
    def __repr__(self):
        pass