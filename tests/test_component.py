import pytest
from osscar.component import Component
from osscar.license import License, LicenseName

def test_component_initialization():
    # Create a TestLicense instance
    license_instance = License(name=LicenseName.MIT, compatible_licenses=[LicenseName.MIT, LicenseName.APACHE_2_0], copyleft=True)
    
    # Create a Component instance
    component = Component(name="ExampleComponent", version="1.0.0", license=license_instance)
    
    # Assert that the component's attributes are set correctly
    assert component.name == "ExampleComponent"
    assert component.version == "1.0.0"
    assert component.license == license_instance

def test_component_repr():
    # Create a TestLicense instance
    license_instance = License(name=LicenseName.MIT, compatible_licenses=[LicenseName.MIT, LicenseName.APACHE_2_0], copyleft=True)
    
    # Create a Component instance
    component = Component(name="ExampleComponent", version="1.0.0", license=license_instance)
    
    # Assert that the string representation is correct
    assert repr(component) == "Component(name=ExampleComponent, version=1.0.0, license=License(LicenseName.MIT))" 