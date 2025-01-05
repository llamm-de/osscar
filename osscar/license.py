from abc import ABC, abstractmethod

class License(ABC):
    @abstractmethod
    def is_compatible(self, other: 'License') -> bool:
        """Check if this license is compatible with another license."""
        pass 

    def __eq__(self, other: object) -> bool:
        """Check if this license is equal to another license."""
        if not isinstance(other, License):
            return False
        return type(self) is type(other) 

    def __repr__(self) -> str:
        """Return the class name as a string."""
        return self.__class__.__name__ 