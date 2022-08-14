#!/usr/bin/env python3
"""
CREATED AT: 2022-08-14

URL: https://leetcode.com/problems/maximum-score-after-splitting-a-string/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1422-MaximumScoreAfterSplittingAString

Difficulty: Easy

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def maxScore(self, s: str) -> int:
        """
        Runtime: 40 ms, faster than 87.11%
        Memory Usage: 13.8 MB, less than 97.61%
        
        2 <= s.length <= 500
        The string s consists of characters '0' and '1' only.
        """
        right_cnt = collections.Counter(s)
        ret, left = 0, 0
        for i in range(len(s) - 1):
            if s[i] == '0':
                left += 1
            right_cnt[s[i]] -= 1
            ret = max(ret, left + right_cnt['1'])
        return ret


def test():
    assert Solution().maxScore(s="011101") == 5
    assert Solution().maxScore(s="00111") == 5
    assert Solution().maxScore(s="1111") == 3


if __name__ == '__main__':
    test()
