import pytest
from osscar.license import License

# Concrete implementation for testing
class TestLicense(License):
    @property
    def compatible_licenses(self) -> list[str]:
        return ["MIT License", "Apache License 2.0", "TestLicense"]

def test_license_equality():
    license1 = TestLicense()
    license2 = TestLicense()
    license3 = TestLicense()

    # Test equality of the same class instances
    assert license1 == license2  # Should be True

    # Test equality with a different instance of the same class
    assert license1 == license3  # Should be True

    # Test equality with a different class
    class AnotherLicense(License):
        @property
        def compatible_licenses(self) -> list[str]:
            return ["GPL License"]

    another_license = AnotherLicense()
    assert license1 != another_license  # Should be False

    # Test equality with a non-License object
    assert license1 != "not a license"  # Should be False 

def test_license_repr():
    license_instance = TestLicense()
    
    # Check the string representation of the license instance
    assert repr(license_instance) == "TestLicense"  # Should match the class name 

def test_is_compatible_with_compatible_license():
    license_instance = TestLicense()
    compatible_license = TestLicense()  # Same class, should be compatible
    assert license_instance.is_compatible(compatible_license)  # Should be True

def test_is_compatible_with_incompatible_license():
    class IncompatibleLicense(License):
        @property
        def compatible_licenses(self) -> list[str]:
            return ["GPL License"]

    incompatible_license = IncompatibleLicense()
    license_instance = TestLicense()
    assert not license_instance.is_compatible(incompatible_license)  # Should be False

def test_is_compatible_with_non_license_object():
    license_instance = TestLicense()
    assert not license_instance.is_compatible("not a license")  # Should be False 