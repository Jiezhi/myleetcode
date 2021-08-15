#!/usr/bin/env python
"""
CREATED AT: 2021/8/15
Des:
https://leetcode.com/contest/weekly-contest-254/problems/number-of-strings-that-appear-as-substrings-in-word/
GITHUB: https://github.com/Jiezhi/myleetcode

"""
from typing import List


class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        cnt = 0
        for p in patterns:
            if p in word:
                cnt += 1
        return cnt


def test():
    assert Solution().numOfStrings(patterns=["a", "b", "c"], word="aaaaabbbbb") == 2
    pass


if __name__ == '__main__':
    test()
