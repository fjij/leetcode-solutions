from typing import List


def rotate_single(matrix: list[list[int]], i: int, j: int) -> None:
    mem = matrix[i][j]
    orientations = [
        (j, -i - 1),
        (-i - 1, -j - 1),
        (-j - 1, i),
        (i, j),
    ]
    for y, x in orientations:
        tmp = matrix[y][x]
        matrix[y][x] = mem
        mem = tmp


def rotate(matrix: list[list[int]]) -> None:
    n = len(matrix)
    for i in range(-(n // -2)):
        for j in range(n // 2):
            print(i, j)
            rotate_single(matrix, i, j)
            print(matrix)


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rotate(matrix)
