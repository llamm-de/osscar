from typing import List
from osscar.component import Component
from osscar.license import License

class Project:
    def __init__(self, components: List[Component]) -> None:
        self.components: List[Component] = components

    def add_component(self, component: Component) -> None:
        """Add a component to the project."""
        self.components.append(component)

    def remove_component(self, component: Component) -> None:
        """Remove a component from the project."""
        self.components.remove(component)

    def get_licenses(self) -> List[License]:
        """Returns a list of unique licenses used by the project's components."""
        # Use a set to eliminate duplicates, then convert back to list
        return list({component.license for component in self.components}) 
    
    def has_copyleft(self) -> bool:
        """Return a boolean whether the project has a copyleft."""
        return any(component.license.copyleft for component in self.components)
    
    def __repr__(self) -> str:
        """Return a string representation of the project."""
        return f"Project(components={self.components})"
    
    def __str__(self) -> str:
        """Return a string representation of the project."""
        return f"Project(components={self.components})"