#!/usr/bin/env python
"""
CREATED AT: 2022/4/27
Des:
https://leetcode.com/problems/longest-palindrome/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

"""
import collections


class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        Runtime: 39 ms, faster than 68.27%
        Memory Usage: 13.8 MB, less than 68.11%

        1 <= s.length <= 2000
        s consists of lowercase and/or uppercase English letters only.
        """
        cnt = collections.Counter(s)
        ret = 0
        for k, v in cnt.items():
            ret += v // 2
        ret *= 2
        return ret if ret == len(s) else ret + 1


def test():
    assert Solution().longestPalindrome("abccccdd") == 7
    assert Solution().longestPalindrome(s="a") == 1


if __name__ == '__main__':
    test()
