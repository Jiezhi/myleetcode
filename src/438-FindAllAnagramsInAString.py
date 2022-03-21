#!/usr/bin/env python
"""
CREATED AT: 2022/3/21
Des:
https://leetcode.com/problems/find-all-anagrams-in-a-string/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""
import collections
import string
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        Runtime: 563 ms, faster than 17.60%
        Memory Usage: 15.2 MB, less than 38.31%

        1 <= s.length, p.length <= 3 * 10^4
        s and p consist of lowercase English letters.
        """
        ret = []
        len_s, len_p = len(s), len(p)
        if len_p > len_s:
            return ret
        cnt_s = collections.Counter(string.ascii_lowercase + s[:len_p])
        cnt_p = collections.Counter(string.ascii_lowercase + p)

        if cnt_s == cnt_p:
            ret.append(0)

        for i in range(len_s - len_p):
            cnt_s[s[i]] -= 1
            cnt_s[s[i + len_p]] += 1

            if cnt_s == cnt_p:
                ret.append(i + 1)

        return ret


def test():
    assert Solution().findAnagrams(s="cbaebabacd", p="abc") == [0, 6]
    assert Solution().findAnagrams(s="abab", p="ab") == [0, 1, 2]


if __name__ == '__main__':
    test()
