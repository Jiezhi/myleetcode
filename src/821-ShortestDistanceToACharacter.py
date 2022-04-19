#!/usr/bin/env python
"""
CREATED AT: 2022/4/19
Des:
https://leetcode.com/problems/shortest-distance-to-a-character/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

"""
from typing import List


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        """
        Runtime: 39 ms, faster than 95.83%
        Memory Usage: 13.9 MB, less than 92.15%

        1 <= s.length <= 10^4
        s[i] and c are lowercase English letters.
        It is guaranteed that c occurs at least once in s.
        """
        ret = [1000] * len(s)
        if s[0] == c:
            ret[0] = 0
        for i in range(1, len(s)):
            if s[i] == c:
                ret[i] = 0
            else:
                ret[i] = ret[i - 1] + 1

        for i in range(len(s) - 2, -1, -1):
            ret[i] = min(ret[i], ret[i + 1] + 1)

        return ret


def test():
    assert Solution().shortestToChar("loveleetcode", "e") == [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]


if __name__ == '__main__':
    test()
