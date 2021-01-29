import unittest

def is_palindrome(s: str) -> bool:
  return s == s[::-1]

class TestIsPalindrome(unittest.TestCase):

  def test_passing(self):
      cases = ['aaa', 'tacocat', 'abcba']
      for case in cases:
        with self.subTest(case):
          self.assertEqual(is_palindrome(case), True)

  def test_failing(self):
      cases = ['aaab', 'tacocats', 'abcbar']
      for case in cases:
        with self.subTest(case):
          self.assertEqual(is_palindrome(case), False)

if __name__ == '__main__':
    unittest.main()