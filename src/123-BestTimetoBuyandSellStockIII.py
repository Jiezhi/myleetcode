#!/usr/bin/env python
"""
CREATED AT: 2021/10/16
Des:

GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Hard

Reference:
Tag: DP

See: 
"""
import sys
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/discuss/39743/Python-DP-solution-120ms

        Runtime: 1383 ms, faster than 44.21%
        Memory Usage: 27.8 MB, less than 87.46%
        1 <= prices.length <= 10**5
        0 <= prices[i] <= 10**5
        :param prices:
        :return:
        """
        min_price = prices[0]
        max_profit = 0
        profits = []
        # first get the max profit if we only use 1 transaction
        for price in prices:
            min_price = min(price, min_price)
            max_profit = max(max_profit, price - min_price)
            profits.append(max_profit)

        curr_max_price = 0
        max_profit = 0
        # we backwards see the max profits if we do more 1 transaction
        for i in range(len(prices) - 1, 0, -1):
            curr_max_price = max(curr_max_price, prices[i])
            max_profit = max(max_profit, curr_max_price - prices[i] + profits[i])
        return max_profit

    def maxProfit2(self, prices: List[int]) -> int:
        """
        https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/discuss/39743/Python-DP-solution-120ms/301157
        :param prices:
        :return:
        """
        one_buy = two_buy = sys.maxsize
        one_profit = two_profit = 0
        for p in prices:
            one_buy = min(one_buy, p)
            one_profit = max(one_profit, p - one_buy)
            two_buy = min(two_buy, p - one_profit)
            two_profit = max(two_profit, p - two_buy)
        return two_profit


def test():
    assert Solution().maxProfit2(prices=[1, 2, 4, 2, 5, 7, 2, 4, 9, 0]) == 13
    assert Solution().maxProfit2(prices=[6, 1, 3, 2, 4, 7]) == 7
    assert Solution().maxProfit2(prices=[3, 3, 5, 0, 0, 3, 1, 4]) == 6
    assert Solution().maxProfit2(prices=[1, 2, 3, 4, 5]) == 4
    assert Solution().maxProfit2(prices=[7, 6, 4, 3, 1]) == 0

    assert Solution().maxProfit(prices=[1, 2, 4, 2, 5, 7, 2, 4, 9, 0]) == 13
    assert Solution().maxProfit(prices=[6, 1, 3, 2, 4, 7]) == 7
    assert Solution().maxProfit(prices=[3, 3, 5, 0, 0, 3, 1, 4]) == 6
    assert Solution().maxProfit(prices=[1, 2, 3, 4, 5]) == 4
    assert Solution().maxProfit(prices=[7, 6, 4, 3, 1]) == 0


if __name__ == '__main__':
    test()
