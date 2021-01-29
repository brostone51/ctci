import unittest

def is_unique(s: str) -> bool:
  ht = {}
  for c in s:
    if c in ht: return False
    ht[c] = True
  return True

class TestIsUnique(unittest.TestCase):

    def test_passing(self):
        cases = ['abcdefg', 'a', 'ab', 'abc', '.,/;', 'aAbB ']
        for case in cases:
          with self.subTest(case):
            self.assertEqual(is_unique(case), True)

    def test_non_passing(self):
        cases = ['aabbccddeeff', 'aa', 'abb', 'abcc', '.,/;;', 'aAbB  ']
        for case in cases:
          with self.subTest(case):
            self.assertEqual(is_unique(case), False)

if __name__ == '__main__':
    unittest.main()