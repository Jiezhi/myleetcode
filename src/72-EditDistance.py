#!/usr/bin/env python
"""
CREATED AT: 2022/3/23
Des:

GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: 

Tag: 

See: 

"""
import sys
from functools import lru_cache

sys.setrecursionlimit(10000)


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        Runtime: 230 ms, faster than 48.50%
        Memory Usage: 16.9 MB, less than 79.25%

        0 <= word1.length, word2.length <= 500
        word1 and word2 consist of lowercase English letters.
        """
        m, n = len(word1), len(word2)

        @lru_cache(None)
        def dp(p1, p2) -> int:
            if p1 >= m and p2 >= n:
                return 0
            if p1 >= m:
                return n - p2
            if p2 >= n:
                return m - p1
            skip_cnt = 0
            while p1 + skip_cnt < m and p2 + skip_cnt < n and word1[p1 + skip_cnt] == word2[p2 + skip_cnt]:
                skip_cnt += 1
            if skip_cnt > 0:
                return dp(p1 + skip_cnt, p2 + skip_cnt)
            return min(1 + dp(p1, p2 + 1), 1 + dp(p1 + 1, p2), dp(p1 + 1, p2 + 1) + 1 if word1[p1] != word2[p2] else 0)

        return dp(0, 0)


def test():
    assert Solution().minDistance("horse", "ros") == 3
    assert Solution().minDistance("intention", "execution") == 5
    w1 = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdef"
    w2 = "bcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefg"
    assert Solution().minDistance(w1, w2) == 2


if __name__ == '__main__':
    test()
