from enum import Enum
from typing import List

class LicenseName(Enum):
    """Enum for the name of the license."""
    MIT = "MIT"
    GPL = "GPL"
    APACHE = "Apache"

class License():
    """Base class for all licenses."""
    def __init__(self, name: LicenseName, compatible_licenses: List[LicenseName], copyleft: bool) -> None:
        self.name = name
        self.compatible_licenses = compatible_licenses
        self.copyleft = copyleft

    def is_compatible(self, other: 'License') -> bool:
        """Check if this license is compatible with another license."""
        if other.name not in self.compatible_licenses:
            return False 
        return True 

    def __eq__(self, other: object) -> bool:
        """Check if this license is equal to another license."""
        return self.name == other.name  
    
    def __hash__(self) -> int:
        """Return a hash of the class name."""
        return hash(self.name)

    def __repr__(self) -> str:
        """Return the class name as a string."""
        return f"License({self.name})"
    
    def __str__(self) -> str:
        """Return the class name as a string."""
        return f"License({self.name})"