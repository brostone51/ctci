import unittest

def string_rotation(s1: str, s2: str) -> bool:
  if len(s1) != len(s2): return False
  return s1 in s2 + s2

class TestStringCompression(unittest.TestCase):

  def test_passing(self):
      cases = [('water', 'erwat'),('waterbottle', 'erbottlewat'),('abcdefg', 'defgabc')]
      for case in cases:
        with self.subTest(case):
          self.assertEqual(string_rotation(case[0], case[1]), True)

  def test_failing(self):
    cases = [('water', 'erwat'),('waterbottle', 'erbottlewat'),('abcdefg', 'defgabc')]
    for case in cases:
      with self.subTest(case):
        self.assertEqual(string_rotation(case[0], case[1]), True)

if __name__ == '__main__':
    unittest.main()