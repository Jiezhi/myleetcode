#!/usr/bin/env python
"""
CREATED AT: 2021/12/10
Des:

https://leetcode.com/problems/domino-and-tromino-tiling/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See:

Ref: https://leetcode.com/problems/domino-and-tromino-tiling/solution/

"""


class Solution:
    def numTilings(self, n: int) -> int:
        """
        Runtime: 36 ms, faster than 63.08% of Python3
        Memory Usage: 14.4 MB, less than 38.97% of Python3

        1 <= n <= 1000
        :param n:
        :return:
        """
        if n <= 2:
            return n
        mod = 10 ** 9 + 7
        dp = [0 for _ in range(n)]
        dp[0] = 1
        dp[1] = 2
        dp2 = [0 for _ in range(n)]
        dp2[1] = 1
        for i in range(2, n):
            dp[i] = (dp[i - 1] + dp[i - 2] + 2 * dp2[i - 1]) % mod
            dp2[i] = (dp[i - 2] + dp2[i - 1]) % mod
        return dp[-1]


def test():
    assert Solution().numTilings(n=4) == 11
    assert Solution().numTilings(n=3) == 5
    assert Solution().numTilings(n=1) == 1


if __name__ == '__main__':
    test()
