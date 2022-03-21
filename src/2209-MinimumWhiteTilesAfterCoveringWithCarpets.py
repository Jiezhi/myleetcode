#!/usr/bin/env python
"""
CREATED AT: 2022/3/21
Des:
https://leetcode.com/problems/minimum-white-tiles-after-covering-with-carpets/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Hard

Tag: 

See: 

"""
from functools import lru_cache


class Solution:
    def minimumWhiteTiles2(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        """
        1 <= carpetLen <= floor.length <= 1000
        floor[i] is either '0' or '1'.
        1 <= numCarpets <= 1000
        """
        # Fixme
        n = len(floor)
        # dp[i][j] i for pos, j for carpet num
        dp = [[0 for _ in range(numCarpets + 1)] for _ in range(n)]
        dp[0][0] = int(floor[0])
        for i in range(1, n):
            dp[i][0] = dp[i - 1][0] + int(floor[i])

        for i in range(1, n):
            for j in range(1, numCarpets + 1):
                dp[i][j] = min(dp[i - 1][j - 1], dp[i][j])
                curr = dp[i - 1][j] + int(floor[i])
                if curr <= dp[i][j]:
                    dp[i][j] = curr
                    for k in range(1, carpetLen):
                        if k + i >= n:
                            break
                        dp[i + k][j] = curr
        return dp[-1][-1]

    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        """
        Ref: https://leetcode.com/problems/minimum-white-tiles-after-covering-with-carpets/discuss/1863955/JavaC%2B%2BPython-DP-solution

        Runtime: 9659 ms, faster than 11.11%
        Memory Usage: 413 MB, less than 22.22%

        1 <= carpetLen <= floor.length <= 1000
        floor[i] is either '0' or '1'.
        1 <= numCarpets <= 1000
        """

        n = len(floor)

        @lru_cache(None)
        def dp(pos, num) -> int:
            if pos <= 0:
                return 0
            return min(dp(pos - 1, num) + int(floor[pos - 1]), dp(pos - carpetLen, num - 1) if num > 0 else n)

        return dp(n, numCarpets)


def test():
    assert Solution().minimumWhiteTiles(floor="100011111001110111111110001100011101111011111111111001001011",
                                        numCarpets=2, carpetLen=3) == 35
    assert Solution().minimumWhiteTiles(floor="10110101", numCarpets=2, carpetLen=2) == 2
    assert Solution().minimumWhiteTiles(floor="11111", numCarpets=2, carpetLen=3) == 0


if __name__ == '__main__':
    test()
