from osscar.project import Project
from osscar.component import Component
from osscar.license import License, LicenseName
from typing import List

def test_project_initialization():
    """Test that a Project can be initialized with a list of components"""
    components = [
        Component("comp1", "1.0", License(name=LicenseName.MIT, compatible_licenses=[LicenseName.MIT, LicenseName.APACHE_2_0], copyleft=True)),
        Component("comp2", "2.0", License(name=LicenseName.MIT, compatible_licenses=[LicenseName.MIT, LicenseName.APACHE_2_0], copyleft=True))
    ]
    project = Project(components)
    assert project.components == components

def test_get_licenses():
    """Test that get_licenses returns unique licenses"""
    # Create a shared license instance
    shared_license = License(name=LicenseName.MIT, compatible_licenses=[LicenseName.MIT, LicenseName.APACHE_2_0], copyleft=True)
    
    # Create components with some shared and some different licenses
    components = [
        Component("comp1", "1.0", shared_license),
        Component("comp2", "2.0", shared_license),
        Component("comp3", "3.0", License(name=LicenseName.APACHE_2_0, compatible_licenses=[LicenseName.APACHE_2_0  ], copyleft=True))
    ]
    
    project = Project(components)
    licenses: List[License] = project.get_licenses()
    
    # Should have 1 unique licenses (MockLicense)
    assert len(licenses) == 2
    assert shared_license in licenses 

def test_add_component():
    """Test that components can be added to the project"""
    project = Project([])
    component = Component("new_comp", "1.0", License(name=LicenseName.MIT, compatible_licenses=[LicenseName.MIT, LicenseName.APACHE_2_0], copyleft=True))
    
    project.add_component(component)
    
    assert len(project.components) == 1
    assert component in project.components

def test_remove_component():
    """Test that components can be removed from the project"""
    component = Component("comp1", "1.0", License(name=LicenseName.MIT, compatible_licenses=[LicenseName.MIT, LicenseName.APACHE_2_0], copyleft=True))
    project = Project([component])
    
    project.remove_component(component)
    
    assert len(project.components) == 0
    assert component not in project.components

def test_has_copyleft_true():
    """Test that has_copyleft returns True when a component has a copyleft license"""
    components = [
        Component("comp1", "1.0", License(name=LicenseName.MIT, compatible_licenses=[LicenseName.MIT, LicenseName.APACHE_2_0], copyleft=True)),
        Component("comp2", "2.0", License(name=LicenseName.APACHE_2_0, compatible_licenses=[LicenseName.APACHE_2_0], copyleft=False))
    ]
    project = Project(components)
    
    assert project.has_copyleft() is True

def test_has_copyleft_false():
    """Test that has_copyleft returns False when no components have a copyleft license"""
    components = [
        Component("comp1", "1.0", License(name=LicenseName.MIT, compatible_licenses=[LicenseName.MIT, LicenseName.APACHE_2_0], copyleft=False)),
        Component("comp2", "2.0", License(name=LicenseName.APACHE_2_0, compatible_licenses=[LicenseName.APACHE_2_0], copyleft=False))
    ]
    project = Project(components)
    
    assert project.has_copyleft() is False 

def test_project_repr():
    components = [
        Component("comp1", "1.0", License(name=LicenseName.MIT, compatible_licenses=[LicenseName.MIT, LicenseName.APACHE_2_0], copyleft=True)),
        Component("comp2", "2.0", License(name=LicenseName.APACHE_2_0, compatible_licenses=[LicenseName.APACHE_2_0], copyleft=True))
    ]
    project = Project(components)
    
    # Assert that the string representation is correct
    assert repr(project) == "Project(components=[Component(name=comp1, version=1.0, license=License(LicenseName.MIT)), Component(name=comp2, version=2.0, license=License(LicenseName.APACHE_2_0))])"

def test_project_str():
    components = [
        Component("comp1", "1.0", License(name=LicenseName.MIT, compatible_licenses=[LicenseName.MIT, LicenseName.APACHE_2_0], copyleft=True)),
        Component("comp2", "2.0", License(name=LicenseName.APACHE_2_0, compatible_licenses=[LicenseName.APACHE_2_0], copyleft=True))
    ]
    project = Project(components)
    
    # Assert that the string representation is correct
    assert str(project) == "Project(components=[Component(name=comp1, version=1.0, license=License(LicenseName.MIT)), Component(name=comp2, version=2.0, license=License(LicenseName.APACHE_2_0))])"
