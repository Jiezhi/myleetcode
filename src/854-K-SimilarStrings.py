#!/usr/bin/env python3
"""
CREATED AT: 2022-09-21

URL: https://leetcode.com/problems/k-similar-strings/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 854-K-SimilarStrings

Difficulty: Hard

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    @cache
    def kSimilarity(self, s1: str, s2: str) -> int:
        """
        https://leetcode.cn/problems/k-similar-strings/solution/xiang-si-du-wei-k-de-zi-fu-chuan-by-leet-8z10/1763167

        Runtime: 1999 ms, faster than 7.27%
        Memory Usage: 66.6 MB, less than 5.11%
        1 <= s1.length <= 20
        s2.length == s1.length
        s1 and s2 contain only lowercase letters from the set {'a', 'b', 'c', 'd', 'e', 'f'}.
        s2 is an anagram of s1.
        """
        if not s1:
            return 0
        if s1[0] == s2[0]:
            return self.kSimilarity(s1[1:], s2[1:])
        return min(1 + self.kSimilarity(s1[1:], s2[1:x] + s2[0] + s2[x + 1:]) for x in range(len(s1)) if s1[0] == s2[x])


def test():
    assert Solution().kSimilarity(s1="ab", s2="ba") == 1
    assert Solution().kSimilarity(s1="abc", s2="bca") == 2
    assert Solution().kSimilarity(s1="abcdefabcdefabcdefab", s2="bafedcbafedcbafedcba") == 10


if __name__ == '__main__':
    test()
