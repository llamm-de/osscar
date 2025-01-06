from osscar.project import Project
from osscar.component import Component
from osscar.license import License
from typing import List

class MockLicense(License):
    """Mock implementation of License for testing"""
    @property
    def copyleft(self) -> bool:
        return False
    
    @property
    def compatible_licenses(self) -> list[str]:
        return ["MockLicense"]

class CopyleftMockLicense(License):
    """Mock implementation of License with copyleft for testing"""
    @property
    def copyleft(self) -> bool:
        return True
    
    @property
    def compatible_licenses(self) -> list[str]:
        return ["MockLicense"]

def test_project_initialization():
    """Test that a Project can be initialized with a list of components"""
    components = [
        Component("comp1", "1.0", MockLicense()),
        Component("comp2", "2.0", MockLicense())
    ]
    project = Project(components)
    assert project.components == components

def test_get_licenses():
    """Test that get_licenses returns unique licenses"""
    # Create a shared license instance
    shared_license = MockLicense()
    
    # Create components with some shared and some different licenses
    components = [
        Component("comp1", "1.0", shared_license),
        Component("comp2", "2.0", shared_license),
        Component("comp3", "3.0", MockLicense())
    ]
    
    project = Project(components)
    licenses: List[License] = project.get_licenses()
    
    # Should have 1 unique licenses (MockLicense)
    assert len(licenses) == 1
    assert shared_license in licenses 

def test_add_component():
    """Test that components can be added to the project"""
    project = Project([])
    component = Component("new_comp", "1.0", MockLicense())
    
    project.add_component(component)
    
    assert len(project.components) == 1
    assert component in project.components

def test_remove_component():
    """Test that components can be removed from the project"""
    component = Component("comp1", "1.0", MockLicense())
    project = Project([component])
    
    project.remove_component(component)
    
    assert len(project.components) == 0
    assert component not in project.components

def test_has_copyleft_true():
    """Test that has_copyleft returns True when a component has a copyleft license"""
    components = [
        Component("comp1", "1.0", MockLicense()),
        Component("comp2", "2.0", CopyleftMockLicense())
    ]
    project = Project(components)
    
    assert project.has_copyleft() is True

def test_has_copyleft_false():
    """Test that has_copyleft returns False when no components have a copyleft license"""
    components = [
        Component("comp1", "1.0", MockLicense()),
        Component("comp2", "2.0", MockLicense())
    ]
    project = Project(components)
    
    assert project.has_copyleft() is False 