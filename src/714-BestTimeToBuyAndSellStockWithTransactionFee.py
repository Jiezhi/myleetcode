#!/usr/bin/env python
"""
CREATED AT: 2022/5/5
Des:
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/solution/

"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        """
        Runtime: 1421 ms, faster than 24.50%
        Memory Usage: 21.3 MB, less than 74.86%

        1 <= prices.length <= 5 * 10^4
        1 <= prices[i] < 5 * 10^4
        0 <= fee < 5 * 10^4
        """
        sell, hold = 0, -prices[0]
        for i, p in enumerate(prices[1:], 1):
            sell = max(sell, hold + p - fee)
            hold = max(hold, sell - p)
        return sell


def test():
    assert Solution().maxProfit([1, 3, 2, 8, 4, 9], 2) == 8


if __name__ == '__main__':
    test()
