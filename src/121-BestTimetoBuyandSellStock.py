#!/usr/bin/env python3
"""
CREATED AT: 2022-09-22

URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
https://leetcode.com/explore/featured/card/top-interview-questions-easy/97/dynamic-programming/572/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 121-BestTimeToBuyAndSellStock

Difficulty: Easy

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        2022-09-22
        1 <= prices.length <= 10^5
        0 <= prices[i] <= 10^4
        """
        hold = 10 ** 4 + 1
        ret = 0
        for p in prices:
            ret = max(ret, p - hold)
            hold = min(p, hold)
        return ret

    def maxProfit2(self, prices: List[int]) -> int:
        """
        2021/8/22
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
