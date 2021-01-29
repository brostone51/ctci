import unittest

def one_away(s1: str, s2: str) -> bool:
  def one_away_same_len(s1: str, s2: str) -> bool:
    miss = 0
    for i in range(len(s1)):
      if s1[i] != s2[i]:
        miss += 1
        if miss > 1: return False
    return True

  def one_away_diff_len(longer: str, shorter: str) -> bool:
    miss = 0
    for i in range(len(shorter)):
      if shorter[i] != longer[i + miss]:
        miss += 1
        if miss > 1: return False
    return True

  if s1 == s2: return True
  elif len(s1) == len(s2):
    return one_away_same_len(s1, s2)
  elif len(s1) - len(s2) == 1:
    return one_away_diff_len(s1, s2)
  elif len(s2) - len(s1) == 1:
    return one_away_diff_len(s2, s1)
  else: return False

class TestOneAway(unittest.TestCase):

    def test_passing(self):
        cases = [('pale', 'ple'),('pales', 'pale'),('pale', 'bale')]
        for case in cases:
          with self.subTest(case):
            self.assertEqual(one_away(case[0], case[1]), True)

    def test_failing(self):
        cases = [('pale', 'bake')]
        for case in cases:
          with self.subTest(case):
            self.assertEqual(one_away(case[0], case[1]), False)

if __name__ == '__main__':
    unittest.main()