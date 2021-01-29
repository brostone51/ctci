import unittest

def is_palindrome_permutation(s: str) -> bool:
  letters = {}
  odd = False
  for c in s:
    letters[c] = letters[c] + 1 if c in letters else 1
  for k, v in letters.items():
    if v % 2 == 1:
      if odd: return False
      odd = True
  return True

def is_palindrome_permutation2(s: str) -> bool:
  letters = {}
  for c in s:
    letters[c] = (letters[c] + 1) % 2 if c in letters else 1
  total = sum([v for k,v in letters.items()])
  return total <= 1

class TestIsPalindromePermuatation(unittest.TestCase):

  def test_passing(self):
      cases = ['aaa', 'tacocat', 'abcba', 'aabbccddeeffgg', 'aabbccddeeffg']
      for case in cases:
        with self.subTest(case):
          self.assertEqual(is_palindrome_permutation(case), True)

  def test_failing(self):
      cases = ['aaab', 'tacocats', 'abcbar', 'aabbccddeefg']
      for case in cases:
        with self.subTest(case):
          self.assertEqual(is_palindrome_permutation(case), False)

class TestIsPalindromePermuatation2(unittest.TestCase):

  def test_passing(self):
      cases = ['aaa', 'tacocat', 'abcba', 'aabbccddeeffgg', 'aabbccddeeffg']
      for case in cases:
        with self.subTest(case):
          self.assertEqual(is_palindrome_permutation2(case), True)

  def test_failing(self):
      cases = ['aaab', 'tacocats', 'abcbar', 'aabbccddeefg']
      for case in cases:
        with self.subTest(case):
          self.assertEqual(is_palindrome_permutation2(case), False)

if __name__ == '__main__':
    unittest.main()