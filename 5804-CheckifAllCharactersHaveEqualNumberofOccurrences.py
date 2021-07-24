#!/usr/bin/env python
"""
CREATED AT: 2021/7/24
Des:

https://leetcode.com/contest/biweekly-contest-57/problems/check-if-all-characters-have-equal-number-of-occurrences/
GITHUB: https://github.com/Jiezhi/myleetcode

"""
from typing import DefaultDict


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d = {}
        for c in s:
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1

        v = d[s[0]]
        for n in d.values():
            if n != v:
                return False
        return True


def test():
    assert Solution().areOccurrencesEqual("abacbc")
    assert not Solution().areOccurrencesEqual("aaabb")
    pass


if __name__ == '__main__':
    test()
