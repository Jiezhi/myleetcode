#!/usr/bin/env python
"""
CREATED AT: 2021/9/9
Des:

https://leetcode.com/problems/search-a-2d-matrix-ii
https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/806/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium
"""
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        129 / 129 test cases passed.
        Status: Accepted
        Runtime: 168 ms
        Memory Usage: 20.6 MB
        :param matrix:
        :param target:
        :return:
        """
        m, n = len(matrix), len(matrix[0])
        if matrix[0][0] > target or matrix[m - 1][n - 1] < target:
            return False

        for i in range(n):
            if matrix[0][i] == target:
                return True
            if matrix[0][i] < target:
                if matrix[m - 1][i] == target:
                    return True
                if matrix[m - 1][i] < target:
                    continue
                l, h = 1, m - 2
                while l <= h:
                    mid = l + (h - l) // 2
                    if matrix[mid][i] == target:
                        return True
                    if matrix[mid][i] < target:
                        l = mid + 1
                    else:
                        h = mid - 1
            else:
                return False


def test():
    assert Solution().searchMatrix(
        matrix=[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]],
        target=19)
    assert Solution().searchMatrix(matrix=[[1, 4], [2, 5]], target=4)
    assert Solution().searchMatrix(matrix=[[1, 4], [2, 5]], target=5)
    assert Solution().searchMatrix(matrix=[[1, 4], [2, 5]], target=2)
    assert Solution().searchMatrix(matrix=[[5], [6]], target=6)
    assert Solution().searchMatrix(matrix=[[5, 6]], target=6)
    assert not Solution().searchMatrix(matrix=[[5], [7]], target=6)
    assert not Solution().searchMatrix(matrix=[[5, 7]], target=6)
    assert Solution().searchMatrix(
        matrix=[[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]],
        target=5)
    assert not Solution().searchMatrix(
        matrix=[[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]],
        target=20)


if __name__ == '__main__':
    test()
