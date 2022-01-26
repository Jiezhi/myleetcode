#!/usr/bin/env python
"""
CREATED AT: 2021/9/13
Des:
https://leetcode.com/problems/unique-paths
https://leetcode.com/explore/interview/card/top-interview-questions-medium/111/dynamic-programming/808/
https://leetcode.com/explore/featured/card/dynamic-programming/634/matrix-path-based-dp/4129/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        62 / 62 test cases passed.
        Status: Accepted
        Runtime: 32 ms
        Memory Usage: 14.4 MB
        :param m:
        :param n:
        :return:
        """
        matrix = [[1 for _ in range(n)] for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]
        return matrix[-1][-1]


def test():
    assert Solution().uniquePaths(m=3, n=7) == 28
    assert Solution().uniquePaths(m=3, n=2) == 3
    assert Solution().uniquePaths(m=7, n=3) == 28
    assert Solution().uniquePaths(m=3, n=3) == 6


if __name__ == '__main__':
    test()
