from abc import ABC, abstractmethod

class License(ABC):
    @property
    @abstractmethod
    def compatible_licenses(self) -> list[str]:
        """Return a list of compatible licenses."""
        pass 

    def is_compatible(self, other: 'License') -> bool:
        """Check if this license is compatible with another license."""
        if str(other) not in self.compatible_licenses:
            return False 
        return True 

    def __eq__(self, other: object) -> bool:
        """Check if this license is equal to another license."""
        if not isinstance(other, License):
            return False
        return type(self) is type(other) 
    
    def __hash__(self) -> int:
        """Return a hash of the class name."""
        return hash(self.__class__.__name__)

    def __repr__(self) -> str:
        """Return the class name as a string."""
        return self.__class__.__name__ 
    
    def __str__(self) -> str:
        """Return the class name as a string."""
        return self.__class__.__name__ 