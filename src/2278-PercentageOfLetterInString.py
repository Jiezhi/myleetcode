#!/usr/bin/env python
"""
CREATED AT: 2022/5/23
Des:

https://leetcode.com/problems/percentage-of-letter-in-string/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

"""
from collections import Counter


class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        """
        85 / 85 test cases passed.
        Status: Accepted 05/23/2022
        Runtime: 40 ms
        Memory Usage: 13.8 MB
        :param s:
        :param letter:
        1 <= s.length <= 100
        s consists of lowercase English letters.
        letter is a lowercase English letter.
        :return:
        """
        return Counter(s)[letter] * 100 // len(s)


def test():
    assert Solution().percentageLetter("abab", "a") == 50


if __name__ == '__main__':
    test()
