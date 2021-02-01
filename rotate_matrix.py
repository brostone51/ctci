import unittest

def rotate_matrix(matrix: list) -> list:
  n = len(matrix)
  rotated = [[] for i in range(n)]
  i = 0
  while i < n:
    for row in matrix[::-1]:
      rotated[i].append(row[i])
    i += 1
  return rotated

class TestRotateMatrix(unittest.TestCase):

  def test_cases(self):
    cases = [
      (
        [[1]],
        [[1]]
      ),
      (
        [
          [1, 2],
          [3, 4]
        ],
        [
          [3, 1],
          [4, 2]
        ]
      ),
      (
        [
          [1, 2, 3],
          [4, 5, 6],
          [7, 8, 9],
        ],
        [
          [7, 4, 1],
          [8, 5, 2],
          [9, 6, 3],
        ],
      )
    ]
    for case in cases:
      with self.subTest(case):
        self.assertEqual(rotate_matrix(case[0]), case[1])

if __name__ == '__main__':
  unittest.main()