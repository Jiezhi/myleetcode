#!/usr/bin/env python
"""
CREATED AT: 2021/8/16
Des:

https://leetcode.com/problems/valid-anagram/
https://leetcode.com/explore/featured/card/top-interview-questions-easy/127/strings/882/
GITHUB: https://github.com/Jiezhi/myleetcode

"""
import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        35 / 35 test cases passed.
        Status: Accepted
        Runtime: 40 ms
        Memory Usage: 14.6 MB
        :param s:
        :param t:
        :return:
        """
        return collections.Counter(s) == collections.Counter(t)


def test():
    assert Solution().isAnagram(s="anagram", t="nagaram")
    assert not Solution().isAnagram(s="rat", t="car")


if __name__ == '__main__':
    test()
