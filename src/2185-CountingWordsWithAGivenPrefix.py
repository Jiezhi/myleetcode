#!/usr/bin/env python
"""
CREATED AT: 2022/2/27
Des:

https://leetcode.com/problems/counting-words-with-a-given-prefix/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

Time Spent:  min
"""
from typing import List


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        """
        Runtime: 52 ms, faster than 55.56%
        Memory Usage: 14.1 MB, less than 22.22%

        1 <= words.length <= 100
        1 <= words[i].length, pref.length <= 100
        words[i] and pref consist of lowercase English letters.
        :param words:
        :param pref:
        :return:
        """
        return sum(1 if x.startswith(pref) else 0 for x in words)


def test():
    assert Solution().prefixCount(words=["pay", "attention", "practice", "attend"], pref="at") == 2


if __name__ == '__main__':
    test()
