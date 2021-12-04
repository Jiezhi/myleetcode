#!/usr/bin/env python
"""
CREATED AT: 2021/11/13
Des:

https://leetcode.com/problems/check-whether-two-strings-are-almost-equivalent/
https://leetcode.com/contest/biweekly-contest-65/problems/check-whether-two-strings-are-almost-equivalent/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 
"""
import collections


class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        """
        n == word1.length == word2.length
        1 <= n <= 100
        word1 and word2 consist only of lowercase English letters.
        :param word1:
        :param word2:
        :return:
        """
        c1 = collections.Counter(word1)
        c2 = collections.Counter(word2)
        for c in range(97, 123):
            cnt1 = c1.get(chr(c)) if c1.get(chr(c)) else 0
            cnt2 = c2.get(chr(c)) if c2.get(chr(c)) else 0
            if abs(cnt2 - cnt1) > 3:
                return False
        return True


def test():
    assert not Solution().checkAlmostEquivalent(word1="aaaa", word2="bccb")
    assert Solution().checkAlmostEquivalent(word1="abcdeef", word2="abaaacc")
    assert Solution().checkAlmostEquivalent(word1="cccddabba", word2="babababab")


if __name__ == '__main__':
    test()
