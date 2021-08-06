#!/usr/bin/env python
"""
CREATED AT: 2021/8/5
Des:

https://leetcode.com/problems/stone-game/
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge-2021/613/week-1-august-1st-august-7th/3870/
GITHUB: https://github.com/Jiezhi/myleetcode
Reference: https://leetcode.com/problems/stone-game/solution/
"""
from functools import lru_cache
from typing import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True

    def stoneGame2(self, piles: List[int]) -> bool:
        """
        Runtime: 544 ms, faster than 32.76% of Python3 online submissions for Stone Game.
        Memory Usage: 125.6 MB, less than 13.10% of Python3 online submissions for Stone Game.
        :param piles:
        :return:
        """

        @lru_cache(None)
        def dp(i, j):
            if i > j:
                return 0
            alex_turn = (j - i) % 2 == 1
            if alex_turn:
                return max(piles[i] + dp(i + 1, j), piles[j] + dp(i, j - 1))
            else:
                return min(dp(i + 1, j) - piles[i], dp(i, j - 1) - piles[j])

        return dp(0, len(piles) - 1) > 0


def test():
    assert Solution().stoneGame(piles=[5, 3, 4, 5])
    assert Solution().stoneGame2(piles=[5, 3, 4, 5])


if __name__ == '__main__':
    test()
