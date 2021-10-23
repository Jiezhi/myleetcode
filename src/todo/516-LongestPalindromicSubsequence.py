#!/usr/bin/env python
"""
CREATED AT: 2021/10/10
Des:
https://leetcode.com/problems/longest-palindromic-subsequence/
https://leetcode.com/study-plan/dynamic-programming/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tags: DP
"""


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """
        1 <= s.length <= 1000
        :param s:
        :return:
        """

        pass


def test():
    assert Solution().longestPalindromeSubseq(s="bbbab") == 4
    assert Solution().longestPalindromeSubseq(s="cbbd") == 2


if __name__ == '__main__':
    test()
