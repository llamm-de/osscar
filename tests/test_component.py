import pytest
from osscar.component import Component
from osscar.license import License

# Concrete implementation for testing
class TestLicense(License):
    @property
    def compatible_licenses(self) -> list[str]:
        return ["MIT License", "Apache License 2.0"]
    
    @property
    def copyleft(self) -> bool:
        return True

def test_component_initialization():
    # Create a TestLicense instance
    license_instance = TestLicense()
    
    # Create a Component instance
    component = Component(name="ExampleComponent", version="1.0.0", license=license_instance)
    
    # Assert that the component's attributes are set correctly
    assert component.name == "ExampleComponent"
    assert component.version == "1.0.0"
    assert component.license == license_instance

def test_component_repr():
    # Create a TestLicense instance
    license_instance = TestLicense()
    
    # Create a Component instance
    component = Component(name="ExampleComponent", version="1.0.0", license=license_instance)
    
    # Assert that the string representation is correct
    assert repr(component) == "Component(name=ExampleComponent, version=1.0.0, license=TestLicense)" 