# test_walletservice.py
"""
Tests for WalletService module.
"""

import unittest
from walletservice import WalletService

class TestWalletService(unittest.TestCase):
    """Test cases for WalletService class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = WalletService()
        self.assertIsInstance(instance, WalletService)
        
    def test_run_method(self):
        """Test the run method."""
        instance = WalletService()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
