# test_chainpro.py
"""
Tests for ChainPro module.
"""

import unittest
from chainpro import ChainPro

class TestChainPro(unittest.TestCase):
    """Test cases for ChainPro class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ChainPro()
        self.assertIsInstance(instance, ChainPro)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ChainPro()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
