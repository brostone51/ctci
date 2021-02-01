import unittest

def zero_matrix(matrix: list) -> list:
  zero_rows = set()
  zero_cols = set()
  for row in range(len(matrix)):
    for col in range(len(matrix[row])):
      if matrix[row][col] is 0:
        zero_rows.add(row)
        zero_cols.add(col)
  for row in zero_rows:
    matrix[row] = [0] * len(matrix[row])
  for col in zero_cols:
    for row in matrix:
      row[col] = 0


class TestRotateMatrix(unittest.TestCase):

  def test_cases(self):
    cases = [
      (
        [[0]],
        [[0]]
      ),
      (
        [
          [1, 2],
          [3, 0]
        ],
        [
          [1, 0],
          [0, 0]
        ]
      ),
      (
        [
          [1, 2, 3],
          [4, 0, 6],
          [7, 8, 9],
        ],
        [
          [1, 0, 3],
          [0, 0, 0],
          [7, 0, 9],
        ],
      )
    ]
    for case in cases:
      with self.subTest(case):
        zero_matrix(case[0])
        self.assertEqual(case[0], case[1])

if __name__ == '__main__':
  unittest.main()