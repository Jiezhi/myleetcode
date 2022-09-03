#!/usr/bin/env python3
"""
CREATED AT: 2022-09-03

URL: https://leetcode.com/problems/maximum-length-of-pair-chain/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 646-MaximumLengthOfPairChain

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        """
        Runtime: 9586 ms, faster than 5.03%
        Memory Usage: 154.6 MB, less than 5.51%

        n == pairs.length
        1 <= n <= 1000
        -1000 <= lefti < righti <= 1000
        """
        pairs.sort()

        @cache
        def dp(cur, pos) -> int:
            if pos == len(pairs):
                return 0

            return max(dp(cur, pos + 1), dp(pairs[pos][1], pos) + 1 if pairs[pos][0] > cur else 0)

        return dp(pairs[0][0] - 1, 0)


def test():
    assert Solution().findLongestChain(pairs=[[1, 2], [2, 3], [3, 4]]) == 2
    assert Solution().findLongestChain(pairs=[[1, 2], [7, 8], [4, 5]]) == 3


if __name__ == '__main__':
    test()
