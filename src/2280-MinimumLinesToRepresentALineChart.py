#!/usr/bin/env python
"""
CREATED AT: 2022/5/23
Des:
https://leetcode.com/problems/minimum-lines-to-represent-a-line-chart/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""
from typing import List


class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        """
        79 / 79 test cases passed.
        Status: Accepted 05/23/2022
        Runtime: 2017 ms
        Memory Usage: 59.4 MB
        :param stockPrices:
        1 <= stockPrices.length <= 10^5
        stockPrices[i].length == 2
        1 <= dayi, pricei <= 10^9
        All dayi are distinct.
        :return:
        """
        n = len(stockPrices)
        if n < 2:
            return 0
        stock = sorted(stockPrices, key=lambda x: x[0])
        ret = 1
        for i, (d, p) in enumerate(stock[2:], 1):
            if (p - stock[i][1]) * (stock[i][0] - stock[i - 1][0]) == (stock[i][1] - stock[i - 1][1]) * (
                    d - stock[i][0]):
                continue
            ret += 1
        return ret


def test():
    assert Solution().minimumLines(stockPrices=[[1, 7], [2, 6], [3, 5], [4, 4], [5, 4], [6, 3], [7, 2], [8, 1]]) == 3


if __name__ == '__main__':
    test()
