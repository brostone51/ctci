import unittest

def string_compression(s1: str) -> str:
  compressed = ''
  current_count = 0
  current_character = -1

  for i in range(len(s1)):
    if current_character == -1: current_character = s1[i]
    if s1[i] != current_character:
      compressed += f'{current_character}{current_count}'
      current_character = -1
      current_count = 0
    current_count += 1

  compressed += f'{current_character}{current_count}'
  current_character = -1
  current_count = 0

  return compressed if len(compressed) < len(s1) else s1

class TestStringCompression(unittest.TestCase):

    def test_passing(self):
        cases = [('aaabbb', 'a3b3'),('aaabbbccc', 'a3b3c3'),('abc', 'abc'), ('aabbcc', 'aabbcc'),('aabbccc', 'a2b2c3')]
        for case in cases:
          with self.subTest(case):
            self.assertEqual(string_compression(case[0]), case[1])

if __name__ == '__main__':
    unittest.main()