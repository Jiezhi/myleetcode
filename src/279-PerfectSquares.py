#!/usr/bin/env python
"""
CREATED AT: 2021/10/14
Des:

https://leetcode.com/problems/perfect-squares/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: DP

See: 322-CoinChange
"""
from typing import List


class Solution:
    def numSquares(self, n: int) -> int:
        """
        Runtime: 5703 ms, faster than 20.74%
        Memory Usage: 14.5 MB, less than 46.28%
        1 <= n <= 10^4
        :param n:
        :return:
        """

        def get_squares() -> List[int]:
            ret = []
            i = 1
            while i * i <= n:
                ret.append(i * i)
                i += 1
            return ret

        squares = get_squares()
        dp = [n for _ in range(n + 1)]
        for square in squares:
            dp[square] = 1
        for i in range(n + 1):
            for square in squares:
                if square > i:
                    break
                if i - square >= 0:
                    dp[i] = min(dp[i], dp[i - square] + 1)
        return dp[-1]


def test():
    assert Solution().numSquares(n=12) == 3
    assert Solution().numSquares(n=13) == 2


if __name__ == '__main__':
    test()
