#!/usr/bin/env python3
"""
CREATED AT: 2022-06-14

URL: https://leetcode.com/problems/delete-operation-for-two-strings/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 583-DeleteOperationForTwoStrings

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from functools import lru_cache


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        Runtime: 431 ms, faster than 39.76%
        Memory Usage: 33.4 MB, less than 6.26%
        1 <= word1.length, word2.length <= 500
        word1 and word2 consist of only lowercase English letters.
        """
        m, n = len(word1), len(word2)

        @lru_cache(None)
        def dp(i, j) -> int:
            if i >= m and j >= n:
                return 0
            if i >= m:
                return n - j
            elif j >= n:
                return m - i
            if word1[i] == word2[j]:
                return dp(i + 1, j + 1)
            else:
                return min(dp(i + 1, j), dp(i, j + 1)) + 1

        return dp(0, 0)


def test():
    assert Solution().minDistance(word1="sea", word2="eat") == 2
    assert Solution().minDistance(word1="leetcode", word2="etco") == 4


if __name__ == '__main__':
    test()
