import pytest
from osscar.license import License

# Concrete implementation for testing
class TestLicense(License):
    def is_compatible(self, other: 'License') -> bool:
        return True  # Placeholder for compatibility logic

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
        def is_compatible(self, other: 'License') -> bool:
            return False  # Placeholder for compatibility logic

    another_license = AnotherLicense()
    assert license1 != another_license  # Should be False

    # Test equality with a non-License object
    assert license1 != "not a license"  # Should be False 


def test_license_repr():
    license_instance = TestLicense()
    
    # Check the string representation of the license instance
    assert repr(license_instance) == "TestLicense"  # Should match the class name 