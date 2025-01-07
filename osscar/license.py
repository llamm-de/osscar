from enum import Enum
from typing import List, Dict
from dataclasses import dataclass

class LicenseName(Enum):
    """Enum for the name of the license."""
    APACHE_1_1 = "Apache-1.1"
    APACHE_2_0 = "Apache-2.0"
    EPL_1_0 = "EPL-1.0"
    EPL_2_0 = "EPL-2.0"
    EUPL_1_1 = "EUPL-1.1"
    EUPL_1_2 = "EUPL-1.2"
    AGPL_3_0 = "AGPL-3.0-only"
    GPL_2_0 = "GPL-2.0"
    GPL_3_0 = "GPL-3.0-only"
    LGPL_2_1 = "LGPL-2.1"
    LGPL_3_0 = "LGPL-3.0-only"
    MIT = "MIT"
    BSD_1_CLAUSE = "BSD-1-Clause"
    BSD_2_CLAUSE = "BSD-2-Clause"
    BSD_3_CLAUSE = "BSD-3-Clause"

@dataclass
class LicenseConfig:
    """Configuration for a license."""
    name: LicenseName
    compatible_licenses: List[LicenseName]
    copyleft: bool

class License():
    """Base class for all licenses."""
    def __init__(self, name: LicenseName, compatible_licenses: List[LicenseName], copyleft: bool) -> None:
        self.name = name
        self.compatible_licenses = compatible_licenses
        self.copyleft = copyleft

    def is_compatible(self, other: 'License') -> bool:
        """Check if this license is compatible with another license."""
        if other.name == self.name:
            return True
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
    
class LicenseFactory:
    """Factory for creating licenses."""

    # License configurations
    # TODO: Add more licenses and complete the configurations for compatibility
    _configs: Dict[LicenseName, LicenseConfig] = {
        LicenseName.MIT: LicenseConfig(name=LicenseName.MIT, compatible_licenses=[], copyleft=False),
        LicenseName.APACHE_2_0: LicenseConfig(name=LicenseName.APACHE_2_0, compatible_licenses=[], copyleft=False),
    }

    @classmethod
    def get_config_from_string(self, license_name: str) -> LicenseConfig:
        """Get the configuration for a license from a string."""
        return self._configs[LicenseName(license_name)]

    @classmethod
    def get_config(self, license_name: LicenseName) -> LicenseConfig:
        """Get the configuration for a license."""
        return self._configs[license_name]
    
    @classmethod
    def create_license_from_string(self, license_name: str) -> License:
        """Create a license from a string."""
        return self.create(LicenseName(license_name))

    @classmethod
    def create(self, license_name: LicenseName) -> License:
        """Create a license by name."""
        if license_name not in self._configs:
            raise ValueError(f"No configuration found for license: {license_name}")
        config = self._configs[license_name]
        return License(name=config.name, compatible_licenses=config.compatible_licenses, copyleft=config.copyleft)
