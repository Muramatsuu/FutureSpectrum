# test_futurespectrum.py
"""
Tests for FutureSpectrum module.
"""

import unittest
from futurespectrum import FutureSpectrum

class TestFutureSpectrum(unittest.TestCase):
    """Test cases for FutureSpectrum class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = FutureSpectrum()
        self.assertIsInstance(instance, FutureSpectrum)
        
    def test_run_method(self):
        """Test the run method."""
        instance = FutureSpectrum()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
