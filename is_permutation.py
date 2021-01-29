import unittest

def is_permutation(s1: str, s2: str) -> bool:
  if s1 == s2: return True
  if len(s1) != len(s2): return False
  s1_ht = {}
  for c in s1:
    s1_ht[c] =  s1_ht[c] + 1 if c in s1_ht else 1
  for c in s2:
    if c not in s1_ht: return False
    s1_ht[c] = s1_ht[c] - 1
    if s1_ht[c] < 0: return False
  return True

def is_permutation2(s1: str, s2: str) -> bool:
  if s1 == s2: return True
  if len(s1) != len(s2): return False

  for c in s2:
    if c not in s1: return False
    s1.replace(c, '', 1)
  return True

class TestIsPermuation(unittest.TestCase):

    def test_passing(self):
        cases = [('aaaa', 'aaaa'),('abc', 'cba'),('abc', 'bac'),('abc', 'cab')]
        for case in cases:
          with self.subTest(case):
            self.assertEqual(is_permutation(case[0], case[1]), True)

    def test_failing(self):
        cases = [('aaaa', 'aaab'),('abc', 'cbaa'),('abca', 'bacr'),('ab4c', 'cabt')]
        for case in cases:
          with self.subTest(case):
            self.assertEqual(is_permutation(case[0], case[1]), False)

class TestIsPermuation2(unittest.TestCase):

    def test_passing(self):
        cases = [('aaaa', 'aaaa'),('abc', 'cba'),('abc', 'bac'),('abc', 'cab')]
        for case in cases:
          with self.subTest(case):
            self.assertEqual(is_permutation2(case[0], case[1]), True)

    def test_failing(self):
        cases = [('aaaa', 'aaab'),('abc', 'cbaa'),('abca', 'bacr'),('ab4c', 'cabt')]
        for case in cases:
          with self.subTest(case):
            self.assertEqual(is_permutation2(case[0], case[1]), False)

if __name__ == '__main__':
    unittest.main()