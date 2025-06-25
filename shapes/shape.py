from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self) ->float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass

    @abstractmethod
    def get_size_info(self) -> str:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass
    
    @abstractmethod
    def __repr__(self) -> str:
        pass