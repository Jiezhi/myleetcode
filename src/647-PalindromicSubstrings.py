#!/usr/bin/env python
"""
CREATED AT: 2022/5/22
Des:
https://leetcode.com/problems/palindromic-substrings/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""
import collections


class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        Runtime: 446 ms, faster than 20.94%
        Memory Usage: 15.4 MB, less than 25.71%
        :param s:
        1 <= s.length <= 1000
        s consists of lowercase English letters.
        :return:
        """
        n = len(s)
        dq = collections.deque((c, i, i) for i, c in enumerate(s))
        for i, c in enumerate(s[:-1]):
            if c == s[i + 1]:
                dq.append((s[i:i + 2], i, i + 1))
        ret = 0
        while dq:
            c, i, j = dq.popleft()
            ret += 1
            if i > 0 and j < n - 1 and s[i - 1] == s[j + 1]:
                dq.append((s[i - 1: j + 2], i - 1, j + 1))
        return ret


def test():
    assert Solution().countSubstrings("abc") == 3
    assert Solution().countSubstrings("aaa") == 6


if __name__ == '__main__':
    test()
