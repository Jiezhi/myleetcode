#!/usr/bin/env python
"""
CREATED AT: 2022/2/11
Des:

https://leetcode.com/problems/permutation-in-string/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

Time Spent:  min
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        CREATED AT: 2022/2/11
        Runtime: 92 ms, faster than 68.01%
        Memory Usage: 14 MB, less than 83.82%

        1 <= s1.length, s2.length <= 10^4
        s1 and s2 consist of lowercase English letters.
        :param s1:
        :param s2:
        :return:
        """
        m, n = len(s1), len(s2)
        if n < m:
            return False
        l1 = [0] * 26
        for c in s1:
            l1[ord(c) - ord('a')] += 1
        for c in s2[:m]:
            l1[ord(c) - ord('a')] -= 1

        if not any(l1):
            return True
        i = 0
        for c in s2[m:]:
            l1[ord(c) - ord('a')] -= 1
            l1[ord(s2[i]) - ord('a')] += 1
            if not any(l1):
                return True
            i += 1

        return False

    def checkInclusion2(self, s1: str, s2: str) -> bool:
        """
        CREATED AT: 2022/2/11
        Runtime: 48 ms, faster than 99.79%
        Memory Usage: 14 MB, less than 93.32%

        1 <= s1.length, s2.length <= 10^4
        s1 and s2 consist of lowercase English letters.
        :param s1:
        :param s2:
        :return:
        """
        m, n = len(s1), len(s2)
        if n < m:
            return False
        l1 = [0] * 26
        for c in s1:
            l1[ord(c) - ord('a')] += 1
        l2 = [0] * 26
        for c in s2[:m]:
            l2[ord(c) - ord('a')] += 1

        if l1 == l2:
            return True
        i = 0
        for c in s2[m:]:
            l2[ord(c) - ord('a')] += 1
            l2[ord(s2[i]) - ord('a')] -= 1
            if l1 == l2:
                return True
            i += 1

        return False


def test():
    assert Solution().checkInclusion(s1="a", s2="a")
    assert not Solution().checkInclusion(s1="a", s2="b")
    assert not Solution().checkInclusion(s1="ab", s2="b")
    assert Solution().checkInclusion(s1="ab", s2="eidbaooo")
    assert not Solution().checkInclusion(s1="ab", s2="eidboaoo")


if __name__ == '__main__':
    test()
