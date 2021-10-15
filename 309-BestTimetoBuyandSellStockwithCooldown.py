#!/usr/bin/env python
"""
CREATED AT: 2021/10/15
Des:
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
GITHUB: https://github.com/Jiezhi/myleetcode

Reference: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/discuss/75942/4-line-Python-solution-52-ms/223885
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/discuss/75942/4-line-Python-solution-52-ms/836890

Difficulty: Medium

Tag: DP

See: 
"""
import math
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        See https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/discuss/75942/4-line-Python-solution-52-ms/836890
        Runtime: 46 ms, faster than 43.75%
        Memory Usage: 14.5 MB, less than 63.31%
        1 <= prices.length <= 5000
        0 <= prices[i] <= 1000
        :param prices:
        :return:
        """
        buy, sell, hold = math.inf, 0, 0
        for p in prices:
            buy = min(buy, p - hold)
            hold = sell
            sell = max(sell, p - buy)
        return sell


def test():
    assert Solution().maxProfit(prices=[6, 1, 3, 2, 4, 7]) == 6
    assert Solution().maxProfit(prices=[1, 2, 3, 0, 2]) == 3
    assert Solution().maxProfit(prices=[3, 8, 9, 0, 5, 10]) == 15
    assert Solution().maxProfit(prices=[1]) == 0
    assert Solution().maxProfit(prices=[1, 2]) == 1
    assert Solution().maxProfit(prices=[1, 2, 4]) == 3


if __name__ == '__main__':
    test()
