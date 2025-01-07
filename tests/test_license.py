import pytest
from osscar.license import License, LicenseName

def test_license_equality():
    license1 = License(name=LicenseName.MIT, compatible_licenses=[LicenseName.MIT, LicenseName.APACHE_2_0], copyleft=True)
    license2 = License(name=LicenseName.MIT, compatible_licenses=[LicenseName.MIT, LicenseName.APACHE_2_0], copyleft=True)
    license3 = License(name=LicenseName.GPL_3_0, compatible_licenses=[LicenseName.GPL_3_0, LicenseName.APACHE_2_0], copyleft=True)

    # Test equality of the same class instances
    assert license1 == license2  # Should be True
    assert license1 != license3  # Should be False

def test_license_repr():
    license_instance = License(name=LicenseName.MIT, compatible_licenses=[LicenseName.MIT, LicenseName.APACHE_2_0], copyleft=True)
    assert repr(license_instance) == "License(LicenseName.MIT)"

def test_is_compatible_with_self():
    license1 = License(name=LicenseName.MIT, compatible_licenses=[LicenseName.MIT, LicenseName.APACHE_2_0], copyleft=True)
    assert license1.is_compatible(license1)  # Should be True

def test_is_compatible_with_compatible_license():
    license1 = License(name=LicenseName.MIT, compatible_licenses=[LicenseName.MIT, LicenseName.APACHE_2_0], copyleft=True)
    license2 = License(name=LicenseName.APACHE_2_0, compatible_licenses=[LicenseName.MIT, LicenseName.APACHE_2_0], copyleft=True)
    assert license1.is_compatible(license2)  # Should be True

def test_is_compatible_with_incompatible_license():
    license1 = License(name=LicenseName.MIT, compatible_licenses=[LicenseName.MIT], copyleft=True)
    license2 = License(name=LicenseName.APACHE_2_0, compatible_licenses=[LicenseName.APACHE_2_0], copyleft=True)
    assert not license1.is_compatible(license2)  # Should be False

def test_license_copyleft_property():
    license1 = License(name=LicenseName.MIT, compatible_licenses=[LicenseName.MIT], copyleft=True)
    assert license1.copyleft  # Should be True
