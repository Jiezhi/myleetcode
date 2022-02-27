#!/usr/bin/env python
"""
CREATED AT: 2022/2/27
Des:

https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram-ii/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

Time Spent:  min
"""
import collections


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        """
        Runtime: 243 ms, faster than 91.67%
        Memory Usage: 16.5 MB, less than 91.67%

        1 <= s.length, t.length <= 2 * 10^5
        s and t consist of lowercase English letters.
        :param s:
        :param t:
        :return:
        """
        source_cnt = collections.Counter(s)
        target_cnt = collections.Counter(t)
        ret = 0
        ord_a = ord('a')
        for i in range(26):
            ret += abs(source_cnt[chr(ord_a + i)] - target_cnt[chr(ord_a + i)])
        return ret


def test():
    assert Solution().minSteps(s="leetcode", t="coats") == 7
    assert Solution().minSteps(s="night", t="thing") == 0


if __name__ == '__main__':
    test()
