#!/usr/bin/env python3
"""
CREATED AT: 2022-09-01

URL: https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1475-FinalPricesWithASpecialDiscountInAShop

Difficulty: Easy

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        """
        Runtime: 76 ms, faster than 61.17%
        Memory Usage: 13.9 MB, less than 64.76%

        1 <= prices.length <= 500
        1 <= prices[i] <= 10^3
        """
        ret = [prices[-1]]
        mono_stack = [prices[-1]]
        for i in range(len(prices) - 2, -1, -1):
            while mono_stack:
                if prices[i] < mono_stack[-1]:
                    mono_stack.pop()
                else:
                    break
            if mono_stack:
                ret.append(prices[i] - mono_stack[-1])
            else:
                ret.append(prices[i])
            mono_stack.append(prices[i])
        return ret[::-1]


def test():
    assert Solution().finalPrices(prices=[8, 4, 6, 2, 3]) == [4, 2, 4, 2, 3]
    assert Solution().finalPrices(prices=[1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert Solution().finalPrices(prices=[10, 1, 1, 6]) == [9, 0, 1, 6]


if __name__ == '__main__':
    test()
