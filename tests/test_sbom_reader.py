import pytest
from osscar.sbom_reader import SBOMReader

# Concrete implementation for testing
class TestSBOMReader(SBOMReader):
    def parse(self, data: str):
        # For testing, we can just return the data as is
        return data

def test_read():
    # Create an instance of the test SBOM reader
    reader = TestSBOMReader()
    
    # Prepare a test SBOM string
    test_data = "test sbom data"
    
    # Write the test data to a temporary file
    with open('test_sbom.txt', 'w') as f:
        f.write(test_data)
    
    # Use the read method to read the data from the file
    result = reader.read('test_sbom.txt')
    
    # Assert that the result matches the expected data
    assert result == test_data

    # Clean up the temporary file
    import os
    os.remove('test_sbom.txt') 