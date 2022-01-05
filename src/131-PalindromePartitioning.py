#!/usr/bin/env python
"""
CREATED AT: 2022/1/5
Des:

https://leetcode.com/problems/palindrome-partitioning/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: DFS

See: 

Time Spent: 20 min
"""
from functools import lru_cache
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        Runtime: 988 ms, faster than 11.63%
        Memory Usage: 31.8 MB, less than 9.65%
        1 <= s.length <= 16
        s contains only lowercase English letters.
        :param s:
        :return:
        """
        ret = []

        @lru_cache(None)
        def is_palindrome(s):
            if not s or len(s) == 1:
                return True
            l, h = 0, len(s) - 1
            while l < h:
                if s[l] != s[h]:
                    return False
                l += 1
                h -= 1
            return True

        def dfs(s: str, prefix: List):
            if not s:
                ret.append(prefix.copy())
                return
            if len(s) == 1:
                tmp_prefix = prefix.copy()
                tmp_prefix.append(s)
                ret.append(tmp_prefix)
                return
            prefix.append(s[0])
            dfs(s[1:], prefix)
            prefix.pop(-1)
            for i in range(2, len(s) + 1):
                if is_palindrome(s[:i]):
                    prefix.append(s[:i])
                    dfs(s[i:], prefix)
                    prefix.pop(-1)

        dfs(s, [])
        return ret


def test():
    assert Solution().partition(s="bb") == [["b", "b"], ["bb"]]
    assert Solution().partition(s="aab") == [["a", "a", "b"], ["aa", "b"]]
    assert Solution().partition(s="a") == [["a"]]


if __name__ == '__main__':
    test()
