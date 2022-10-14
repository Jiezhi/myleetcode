#!/usr/bin/env python
"""
CREATED AT: 2021/10/10
Des:
https://leetcode.com/problems/longest-palindromic-substring/
https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/780/
https://leetcode.com/study-plan/dynamic-programming/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tags: DP
"""
from tool import *


class Solution:
    @lru_cache(None)
    def isPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True
        if s[0] != s[-1]:
            return False
        return self.isPalindrome(s[1:-1])

    def longestPalindrome(self, s: str) -> str:
        """
        Runtime: 360 ms, faster than 92.14% of Python3 online submissions
        Memory Usage: 37.4 MB, less than 5.51% of Python3 online submissions
        1 <= s.length <= 1000
        :param s:
        :return:
        """

        if self.isPalindrome(s):
            return s
        longest = s[0]
        for i in range(len(s) - 1):
            k = 1
            right_shift = 0
            while i + right_shift + 1 < len(s) and s[i + right_shift + 1] == s[i]:
                right_shift += 1
            tmp_longest = s[i:i + right_shift + 1]
            while i - k >= 0 and i + k + right_shift < len(s):
                if self.isPalindrome(s[i - k] + tmp_longest + s[i + k + right_shift]):
                    tmp_longest = s[i - k] + tmp_longest + s[i + k + right_shift]
                    k += 1
                else:
                    break
            if len(tmp_longest) > len(longest):
                longest = tmp_longest
        return longest

    def longestPalindrome2(self, s):
        """
        20221014 HW 二面
        执行用时：620 ms 在所有 Python3 提交中击败了 67.04% 用户
        内存消耗：62 MB 在所有 Python3 提交中击败了 5.06%用户
        通过测试用例：40 / 140
        1 <= s.length <= 1000
        s 仅由数字和英文字母组成
        :type s: str
        :rtype: str
        """

        ret = (1, s[0])

        @cache
        def isPalindrome(i, j) -> bool:
            if i == j:
                return True
            if not 0 <= i <= j < len(s):
                return True

            return s[i] == s[j] and isPalindrome(i + 1, j - 1)

        pos = collections.defaultdict(list)
        for i, c in enumerate(s):
            pos[c].append(i)

        for i, c in enumerate(s):
            p = pos[c]
            for j in p[::-1]:
                if i >= j or j - i + 1 < ret[0]:
                    break
                if isPalindrome(i, j) and j - i + 1 > ret[0]:
                    ret = (j - i + 1, s[i:j + 1])
                    break

        return ret[1]


def test():
    assert Solution().longestPalindrome(s="bb") == 'bb'
    assert Solution().longestPalindrome(s="abb") == 'bb'
    assert Solution().longestPalindrome(s="bppbsooos") == 'sooos'
    assert Solution().longestPalindrome(s="ac") == 'a'
    assert Solution().longestPalindrome(s="bba") == 'bb'
    assert Solution().longestPalindrome(s="babad") == 'bab'
    assert Solution().longestPalindrome(s="zzdjdofaodjfoajsdfoajsdofjasodbabadjdoafjowejoajweofjaweofjaowe") == 'djd'
    assert Solution().longestPalindrome(s="cbbd") == 'bb'
    assert Solution().longestPalindrome(s="a") == 'a'


if __name__ == '__main__':
    test()
