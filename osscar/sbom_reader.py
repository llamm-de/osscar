from abc import ABC, abstractmethod
from typing import Any

class SBOMReader(ABC):
    @abstractmethod
    def parse(self, data: str) -> Any:
        """Parse the SBOM data into a usable format."""
        pass

    def read(self, file_path: str) -> Any:
        """Read the SBOM data from the specified file."""
        with open(file_path, 'r') as file:
            data = file.read()
        return self.parse(data) 