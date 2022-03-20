#!/usr/bin/env python
"""
CREATED AT: 2022/3/20
Des:
https://leetcode.com/problems/maximize-number-of-subsequences-in-a-string/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 🏆 Biweekly Contest 74

See: 

"""
import collections


class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        """
        1 <= text.length <= 10^5
        pattern.length == 2
        text and pattern consist only of lowercase English letters.
        """
        l = []
        for c in text:
            if c in pattern:
                l.append(c)
        p1, p2 = pattern[0], pattern[1]
        if p1 == p2:
            return (len(l) + 1) * len(l) // 2

        cnt = collections.Counter(l)

        p1_cnt = cnt[p1]
        p2_cnt = cnt[p2]
        ret = 0
        for c in l:
            if c == pattern[0]:
                ret += cnt[p2]
            else:
                cnt[p2] -= 1
        return max(p1_cnt, p2_cnt) + ret


def test():
    assert Solution().maximumSubsequenceCount(text="abdcdbc", pattern="ac") == 4
    assert Solution().maximumSubsequenceCount(text="aabb", pattern="ab") == 6


if __name__ == '__main__':
    test()
