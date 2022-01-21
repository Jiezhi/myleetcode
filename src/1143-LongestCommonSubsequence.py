#!/usr/bin/env python
"""
CREATED AT: 2022/1/21
Des:

https://leetcode.com/problems/longest-common-subsequence/
https://leetcode.com/explore/featured/card/dynamic-programming/631/strategy-for-solving-dp-problems/4045/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

Time Spent:  min
"""
from functools import lru_cache


class Solution:
    def longestCommonSubsequence2(self, text1: str, text2: str) -> int:
        """
        CREATED AT: 2022/1/21
        Runtime: 436 ms, faster than 66.06%
        Memory Usage: 22.7 MB, less than 55.90%

        1 <= text1.length, text2.length <= 1000
        text1 and text2 consist of only lowercase English characters.
        :param text1:
        :param text2:
        :return:
        """
        # bottom to top
        dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
        return dp[-1][-1]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        CREATED AT: 2022/1/21
        44 / 44 test cases passed.
        Status: Accepted
        Runtime: 1613 ms
        Memory Usage: 141.7 MB

        1 <= text1.length, text2.length <= 1000
        text1 and text2 consist of only lowercase English characters.
        :param text1:
        :param text2:
        :return:
        """

        # top to bottom
        @lru_cache(None)
        def dp(i, j):
            if i < 0 or j < 0:
                return 0
            if text1[i] == text2[j]:
                ret = dp(i - 1, j - 1) + 1
            else:
                ret = max(dp(i - 1, j), dp(i, j - 1))
            return ret

        return dp(len(text1) - 1, len(text2) - 1)


def test():
    assert Solution().longestCommonSubsequence2(text1="abcde", text2="a") == 1
    assert Solution().longestCommonSubsequence2(text1="abcde", text2="abcde") == 5
    assert Solution().longestCommonSubsequence2(text1="abcde", text2="ace") == 3
    assert Solution().longestCommonSubsequence2(text1="abc", text2="abc") == 3
    assert Solution().longestCommonSubsequence2(text1="abc", text2="def") == 0

    assert Solution().longestCommonSubsequence(text1="abcde", text2="a") == 1
    assert Solution().longestCommonSubsequence(text1="abcde", text2="abcde") == 5
    assert Solution().longestCommonSubsequence(text1="abcde", text2="ace") == 3
    assert Solution().longestCommonSubsequence(text1="abc", text2="abc") == 3
    assert Solution().longestCommonSubsequence(text1="abc", text2="def") == 0


if __name__ == '__main__':
    test()
