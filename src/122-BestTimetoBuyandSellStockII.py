#!/usr/bin/env python
"""
Created on 2020/12/2

Des:  https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/564/


"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Buy before price increase, sell before price decrease, you win!
        l = len(prices)
        if l == 1:
            return 0
        win = 0
        to_buy = True
        buy = 0
        for i in range(l - 1):
            if to_buy:
                if prices[i] < prices[i + 1]:
                    buy = prices[i]
                    to_buy = False
            else:
                if prices[i] > prices[i + 1]:
                    win += prices[i] - buy
                    to_buy = True
        if not to_buy:
            win += prices[-1] - buy
        return win


def test():
    assert Solution().maxProfit([1, 2]) == 1
    assert Solution().maxProfit([2, 1]) == 0
    assert Solution().maxProfit([7, 1, 5, 3, 6, 4]) == 7
    assert Solution().maxProfit([1, 2, 3, 4, 5]) == 4
    assert Solution().maxProfit([7, 6, 4, 3, 1]) == 0


if __name__ == '__main__':
    test()
