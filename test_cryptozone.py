# test_cryptozone.py
"""
Tests for CryptoZone module.
"""

import unittest
from cryptozone import CryptoZone

class TestCryptoZone(unittest.TestCase):
    """Test cases for CryptoZone class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CryptoZone()
        self.assertIsInstance(instance, CryptoZone)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CryptoZone()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
