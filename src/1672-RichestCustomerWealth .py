#!/usr/bin/env python
"""
CREATED AT: 2022/1/31
Des:

https://leetcode.com/problems/richest-customer-wealth/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

Time Spent: 1 min
"""
from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        """
        Runtime: 101 ms, faster than 10.32%
        Memory Usage: 13.9 MB, less than 96.85%
        m == accounts.length
        n == accounts[i].length
        1 <= m, n <= 50
        1 <= accounts[i][j] <= 100
        :param accounts:
        :return:
        """
        return max(sum(x) for x in accounts)


def test():
    assert Solution().maximumWealth(accounts=[[1, 2, 3], [3, 2, 1]]) == 6
    assert Solution().maximumWealth(accounts=[[1, 5], [7, 3], [3, 5]]) == 10
    assert Solution().maximumWealth(accounts=[[2, 8, 7], [7, 1, 3], [1, 9, 5]]) == 17


if __name__ == '__main__':
    test()
