#!/usr/bin/env python
"""
CREATED AT: 2021/10/16
Des:

https://leetcode.com/problemset/all/?search=2039.+The+Time+When+the+Network+Becomes+Idle&page=1#:~:text=Medium-,2039.%20The%20Time%20When%20the%20Network%20Becomes%20Idle,-45.9%25
https://leetcode.com/contest/biweekly-contest-63/problems/the-time-when-the-network-becomes-idle/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 
"""
from typing import List


class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        """
        n == patience.length
        2 <= n <= 10**5
        patience[0] == 0
        1 <= patience[i] <= 10**5 for 1 <= i < n
        1 <= edges.length <= min(10**5, n * (n - 1) / 2)
        edges[i].length == 2
        0 <= ui, vi < n
        ui != vi
        There are no duplicate edges.
        Each server can directly or indirectly reach another server.
        :param edges:
        :param patience:
        :return:
        """
        pass


def test():
    assert Solution().networkBecomesIdle(edges=[[0, 1], [1, 2]], patience=[0, 2, 1]) == 8
    assert Solution().networkBecomesIdle(edges=[[0, 1], [0, 2], [1, 2]], patience=[0, 10, 10]) == 3


if __name__ == '__main__':
    test()
