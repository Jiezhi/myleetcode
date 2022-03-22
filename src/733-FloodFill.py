#!/usr/bin/env python
"""
CREATED AT: 2022/3/22
Des:
https://leetcode.com/problems/flood-fill/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

"""
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        """
        Runtime: 147 ms, faster than 12.40%
        Memory Usage: 14.2 MB, less than 45.66%

        m == image.length
        n == image[i].length
        1 <= m, n <= 50
        0 <= image[i][j], newColor < 2^16
        0 <= sr < m
        0 <= sc < n
        """
        m, n = len(image), len(image[0])
        to_fill = set()
        color = image[sr][sc]

        def fill(r, c):
            if (r, c) in to_fill:
                return
            to_fill.add((r, c))
            if r > 0 and image[r - 1][c] == color:
                fill(r - 1, c)
            if c > 0 and image[r][c - 1] == color:
                fill(r, c - 1)
            if r < m - 1 and image[r + 1][c] == color:
                fill(r + 1, c)
            if c < n - 1 and image[r][c + 1] == color:
                fill(r, c + 1)

        fill(sr, sc)
        for i, j in to_fill:
            image[i][j] = newColor
        return image


def test():
    assert Solution().floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2) == [[2, 2, 2], [2, 2, 0], [2, 0, 1]]


if __name__ == '__main__':
    test()
