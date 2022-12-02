#!/usr/bin/env python3
"""
CREATED AT: 2022-12-02

URL: https://leetcode.com/problems/determine-if-two-strings-are-close/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1657-DetermineIfTwoStringsAreClose

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        """
        1 <= word1.length, word2.length <= 10^5
        word1 and word2 contain only lowercase English letters.
        """
        if len(word1) != len(word2):
            return False
        cnt1, cnt2 = Counter(word1), Counter(word2)
        return set(cnt1.keys()) == set(cnt2.keys()) and sorted(Counter(word1).values()) == sorted(
            Counter(word2).values())


def test():
    assert Solution().closeStrings(word1="abc", word2="bca")


if __name__ == '__main__':
    test()
