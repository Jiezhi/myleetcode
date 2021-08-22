#!/usr/bin/env python
"""
CREATED AT: 2021/8/22
Des:

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
https://leetcode.com/explore/featured/card/top-interview-questions-easy/97/dynamic-programming/572/
GITHUB: https://github.com/Jiezhi/myleetcode

"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        211 / 211 test cases passed.
        Status: Accepted
        Runtime: 920 ms
        Memory Usage: 25.2 MB
        :param prices:
        :return:
        """
        n = len(prices)
        if n <= 1:
            return 0
        buy = prices[0]
        sell = prices[1]
        profit = sell - buy
        for i in range(1, n):
            if prices[i] < buy and i < n - 1:
                buy = prices[i]
                sell = prices[i + 1]
                profit = max(profit, sell - buy)
            elif prices[i] > sell:
                sell = prices[i]
                profit = max(profit, sell - buy)
        return profit if profit > 0 else 0


def test():
    assert Solution().maxProfit(prices=[7, 1, 5, 3, 6, 4]) == 5
    assert Solution().maxProfit(prices=[7, 6, 4, 3, 1]) == 0
    assert Solution().maxProfit(prices=[1, 2, 4]) == 3


if __name__ == '__main__':
    test()
