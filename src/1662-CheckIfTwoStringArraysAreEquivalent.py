#!/usr/bin/env python3
"""
CREATED AT: 2022-10-25

URL: https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1662-CheckIfTwoStringArraysAreEquivalent

Difficulty: Easy

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        """
        Runtime: 39 ms, faster than 85.79%
        Memory Usage: 13.8 MB, less than 75.82%

        1 <= word1.length, word2.length <= 10^3
        1 <= word1[i].length, word2[i].length <= 10^3
        1 <= sum(word1[i].length), sum(word2[i].length) <= 10^3
        word1[i] and word2[i] consist of lowercase letters.
        """
        return ''.join(word1) == ''.join(word2)


def test():
    assert Solution().arrayStringsAreEqual(word1=["ab", "c"], word2=["a", "bc"])
    assert not Solution().arrayStringsAreEqual(word1=["a", "cb"], word2=["ab", "c"])
    assert Solution().arrayStringsAreEqual(word1=["abc", "d", "defg"], word2=["abcddefg"])


if __name__ == '__main__':
    test()
