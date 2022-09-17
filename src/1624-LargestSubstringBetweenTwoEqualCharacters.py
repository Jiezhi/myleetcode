#!/usr/bin/env python3
"""
CREATED AT: 2022-09-17

URL: https://leetcode.com/problems/largest-substring-between-two-equal-characters/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1624-LargestSubstringBetweenTwoEqualCharacters

Difficulty: Easy

Desc: 

Tag: 

See: 

"""


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        """
        Runtime: 64 ms, faster than 28.05%
        Memory Usage: 13.9 MB, less than 62.54%
        1 <= s.length <= 300
        s contains only lowercase English letters.
        """
        ret = -1
        chars = {}
        for i, c in enumerate(s):
            if c not in chars:
                chars[c] = i
            else:
                ret = max(ret, i - chars[c] - 1)
        return ret


def test():
    assert Solution().maxLengthBetweenEqualCharacters(s="aa") == 0
    assert Solution().maxLengthBetweenEqualCharacters(s="abca") == 2
    assert Solution().maxLengthBetweenEqualCharacters(s="cbzxy") == -1


if __name__ == '__main__':
    test()
