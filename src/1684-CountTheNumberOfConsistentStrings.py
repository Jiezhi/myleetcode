#!/usr/bin/env python3
"""
CREATED AT: 2022-11-08

URL: https://leetcode.com/problems/count-the-number-of-consistent-strings/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1684-CountTheNumberOfConsistentStrings

Difficulty: Easy

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        """
        Runtime: 723 ms, faster than 15.25%
        Memory Usage: 16.1 MB, less than 8.18%

        1 <= words.length <= 10^4
        1 <= allowed.length <= 26
        1 <= words[i].length <= 10
        The characters in allowed are distinct.
        words[i] and allowed contain only lowercase English letters.
        """
        allowed = set(allowed)
        return sum(1 for word in words if all(c in allowed for c in word))


def test():
    assert Solution().countConsistentStrings(allowed="ab", words=["ad", "bd", "aaab", "baa", "badab"]) == 2
    assert Solution().countConsistentStrings(allowed="abc", words=["a", "b", "c", "ab", "ac", "bc", "abc"]) == 7
    assert Solution().countConsistentStrings(allowed="cad",
                                             words=["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"]) == 4


if __name__ == '__main__':
    test()
