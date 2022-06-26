#!/usr/bin/env python3
"""
CREATED AT: 2022-06-26

URL: https://leetcode.com/problems/count-number-of-ways-to-place-houses/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 2320-CountNumberOfWaysToPlaceHouses

Difficulty: Medium

Desc: 

Tag: 

See: 

"""


class Solution:
    def countHousePlacements(self, n: int) -> int:
        """
        1 <= n <= 10^4
        :param n:
        :return:
        """
        MOD = 10 ** 9 + 7

        if n <= 2:
            return (n + 1) ** 2

        dp = [0] * (n + 1)
        dp[1] = 2
        dp[2] = 3

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[-1] ** 2 % MOD


def test():
    assert Solution().countHousePlacements(n=1) == 4
    assert Solution().countHousePlacements(n=2) == 9


if __name__ == '__main__':
    test()
