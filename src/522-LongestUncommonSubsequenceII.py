#!/usr/bin/env python
"""
CREATED AT: 2021/8/28
Des:
https://leetcode.com/problems/longest-uncommon-subsequence-ii/

GITHUB: https://github.com/Jiezhi/myleetcode

See: 521
"""
from typing import List


class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        """
        Solved at 2022/3/5
        Runtime: 46 ms, faster than 66.84%
        Memory Usage: 13.8 MB, less than 91.58%

        2 <= strs.length <= 50
        1 <= strs[i].length <= 10
        strs[i] consists of lowercase English letters.
        """
        uni_set = set()
        dup_set = set()
        for s in strs:
            if s in dup_set:
                continue
            if s in uni_set:
                uni_set.remove(s)
                dup_set.add(s)
            else:
                uni_set.add(s)

        if not dup_set:
            return max(len(x) for x in strs)

        def isSubs(s, t) -> bool:
            i, j = 0, 0
            while i < len(s) and j < len(t):
                if s[i] == t[j]:
                    i += 1
                    j += 1
                else:
                    j += 1
            return i == len(s)

        # exists duplication
        for s in sorted(strs, key=lambda x: len(x), reverse=True):
            if s in dup_set:
                continue
            lus = True
            for dup in dup_set:
                if len(dup) > len(s) and isSubs(s, dup):
                    lus = False
                    break
            if lus:
                return len(s)

        return -1


def test():
    assert Solution().findLUSlength(strs=["aba", "cdc", "eae"]) == 3
    assert Solution().findLUSlength(strs=["aaa", "aaa", "aa"]) == -1


if __name__ == '__main__':
    test()
