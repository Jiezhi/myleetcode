#!/usr/bin/env python
"""
CREATED AT: 2021/10/18
Des:

https://leetcode.com/problems/search-a-2d-matrix/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: BinarySearch

See: 
"""
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Runtime: 65 ms, faster than 23.57%
        Memory Usage: 14.7 MB, less than 63.41%

        Integers in each row are sorted from left to right.
        The first integer of each row is greater than the last integer of the previous row.
        m == matrix.length
        n == matrix[i].length
        1 <= m, n <= 100
        -10**4 <= matrix[i][j], target <= 10**4
        :param matrix:
        :param target:
        :return:
        """
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        m, n = len(matrix), len(matrix[0])
        l, h = 0, m - 1
        while l <= h:
            mid = l + (h - l) // 2
            if matrix[mid][0] == target:
                return True
            if matrix[mid][0] < target:
                l = mid + 1
            else:
                h = mid - 1
        # line l
        if l >= m or matrix[l][0] > target:
            row = l - 1
        else:
            row = l
        l, h = 0, n - 1
        while l <= h:
            mid = l + (h - l) // 2
            if matrix[row][mid] == target:
                return True
            if matrix[row][mid] < target:
                l = mid + 1
            else:
                h = mid - 1
        return False


def test():
    assert not Solution().searchMatrix(matrix=[[1, 3]], target=2)
    assert not Solution().searchMatrix(matrix=[[1], [3]], target=2)
    assert Solution().searchMatrix(matrix=[[1], [3]], target=1)
    assert Solution().searchMatrix(matrix=[[1], [3]], target=3)
    assert Solution().searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=3)
    assert Solution().searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [21, 22, 23, 24], [25, 30, 34, 60]],
                                   target=16)
    assert not Solution().searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=13)

    if __name__ == '__main__':
        test()
