import unittest
from ddt import ddt, data, unpack

from source import palindrome as func


@ddt
class TestPalindrome(unittest.TestCase):
    @data(
        ('aabaa', True),
        ('abac', False),
        ('c', True),
        ('testmeplease', False),
        ('hlbeeykoqqqokyeeblh', True),
    )
    
    @unpack
    def test_positive(self, inputString, result) -> None:
        self.assertEqual(func.checkPalindrome(inputString), result)
    
    @data(
        ('', False),
        (None, False),
    )
    
    @unpack
    def test_negative(self, inputString, result) -> None:
        if inputString is None:
          self.assertEqual(func.checkPalindrome(), result)
        else:
          self.assertEqual(func.checkPalindrome(inputString), result)

if __name__ == '__main__':
    unittest.main()
