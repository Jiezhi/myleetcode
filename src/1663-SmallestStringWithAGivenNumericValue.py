#!/usr/bin/env python
"""
CREATED AT: 2022/3/22
Des:
https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""


class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        """
        Runtime: 56 ms, faster than 90.32%
        Memory Usage: 14.8 MB, less than 99.54%
        1 <= n <= 10^5
        n <= k <= 26 * n
        """
        zcnt, k = divmod(k - n, 25)
        if zcnt == n:
            return "z" * zcnt
        return f'{"a" * (n - zcnt - 1)}{chr(ord("a") + k)}{"z" * zcnt}'


def test():
    assert Solution().getSmallestString(n=3, k=27) == "aay"
    assert Solution().getSmallestString(n=5, k=73) == "aaszz"
    assert Solution().getSmallestString(n=5, k=130) == "zzzzz"


if __name__ == '__main__':
    test()
