import pytest
from osscar.license import LicenseFactory, LicenseName, License

def test_get_config_from_string_valid():
    """Test getting a valid license configuration from a string."""
    config = LicenseFactory.get_config_from_string("MIT")
    assert config.name == LicenseName.MIT
    assert not config.copyleft
    assert config.compatible_licenses == []

def test_get_config_from_string_invalid():
    """Test getting a license configuration from an invalid string."""
    with pytest.raises(ValueError):
        LicenseFactory.get_config_from_string("INVALID_LICENSE")

def test_get_config_valid():
    """Test getting a valid license configuration."""
    config = LicenseFactory.get_config(LicenseName.APACHE_2_0)
    assert config.name == LicenseName.APACHE_2_0
    assert not config.copyleft
    assert config.compatible_licenses == []

def test_get_config_invalid():
    """Test getting a license configuration for an invalid license name."""
    with pytest.raises(KeyError):
        LicenseFactory.get_config(LicenseName.EUPL_1_1)

def test_create_license_from_string_valid():
    """Test creating a license from a valid string."""
    license = LicenseFactory.create_license_from_string("MIT")
    assert license.name == LicenseName.MIT

def test_create_license_from_string_invalid():
    """Test creating a license from an invalid string."""
    with pytest.raises(ValueError):
        LicenseFactory.create_license_from_string("INVALID_LICENSE")

def test_create_license_valid():
    """Test creating a license from a valid LicenseName."""
    license = LicenseFactory.create(LicenseName.APACHE_2_0)
    assert license.name == LicenseName.APACHE_2_0

def test_create_license_invalid():
    """Test creating a license from an invalid LicenseName."""
    with pytest.raises(ValueError):
        LicenseFactory.create(LicenseName.EUPL_1_1)
