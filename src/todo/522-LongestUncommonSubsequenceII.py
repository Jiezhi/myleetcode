#!/usr/bin/env python
"""
CREATED AT: 2021/8/28
Des:
https://leetcode.com/problems/longest-uncommon-subsequence-ii/

GITHUB: https://github.com/Jiezhi/myleetcode

"""
from typing import List


class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        pass


def test():
    assert Solution().findLUSlength(strs=["aba", "cdc", "eae"]) == 3
    assert Solution().findLUSlength(strs=["aaa", "aaa", "aa"]) == -1


if __name__ == '__main__':
    test()
