#!/usr/bin/env python
"""
CREATED AT: 2022/1/21
Des:

https://leetcode.com/problems/word-break/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

Time Spent:  min
"""
from functools import lru_cache
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        CREATED AT: 2022/1/21
        45 / 45 test cases passed.
        Status: Accepted
        Runtime: 146 ms
        Memory Usage: 14.5 MB
        1 <= s.length <= 300
        1 <= wordDict.length <= 1000
        1 <= wordDict[i].length <= 20
        s and wordDict[i] consist of only lowercase English letters.
        All the strings of wordDict are unique.
        :param s:
        :param wordDict:
        :return:
        """
        n = len(s)
        min_length, max_length = 1000, 1
        for word in wordDict:
            if min_length > len(word):
                min_length = len(word)
            if max_length < len(word):
                max_length = len(word)

        # bottom to top
        dp = [[False for _ in range(n + 1)] for _ in range(n)]
        dp[0][0] = True
        for i in range(n):
            for j in range(i + min_length, min(i + max_length, n) + 1):
                dp[i][j] = s[i:j] in wordDict and any(dp[x][i] for x in range(i + 1))
                # Or switch below
                # if s[i:j] in wordDict:
                #     for k in range(i + 1):
                #         if dp[k][i]:
                #             dp[i][j] = True
                #             break
            if dp[i][-1]:
                return True
        return False

    def wordBreak2(self, s: str, wordDict: List[str]) -> bool:
        """
        CREATED AT: 2022/1/21
        Runtime: 70 ms, faster than 16.20%
        Memory Usage: 14.9 MB, less than 5.84%

        1 <= s.length <= 300
        1 <= wordDict.length <= 1000
        1 <= wordDict[i].length <= 20
        s and wordDict[i] consist of only lowercase English letters.
        All the strings of wordDict are unique.
        :param s:
        :param wordDict:
        :return:
        """
        n = len(s)
        min_length, max_length = 1000, 1
        for word in wordDict:
            if min_length > len(word):
                min_length = len(word)
            if max_length < len(word):
                max_length = len(word)

        # top to bottom
        @lru_cache(None)
        def dp(i) -> bool:
            if i >= n:
                return True
            if n - i < min_length:
                return False
            return any((s[i:j] in wordDict and dp(j) for j in range(i + min_length, min(i + max_length, n + 1) + 1)))

        return dp(0)


def test():
    assert Solution().wordBreak(s="aaaaaaa", wordDict=["aaaa", "aaa"])
    assert Solution().wordBreak(s="leetcode", wordDict=["leet", "code"])
    assert Solution().wordBreak(s="applepenapple", wordDict=["apple", "pen"])
    assert not Solution().wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"])


if __name__ == '__main__':
    test()
