#!/usr/bin/env python
"""
CREATED AT: 2022/1/21
Des:

https://leetcode.com/problems/gas-station/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

Time Spent:  min
"""
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        CREATED AT: 2022/1/21
        Runtime: 920 ms, faster than 8.13%
        Memory Usage: 19 MB, less than 16.63%

        gas.length == n
        cost.length == n
        1 <= n <= 10^5
        0 <= gas[i], cost[i] <= 10^4
        :param gas:
        :param cost:
        :return:
        """
        n = len(cost)
        if sum(gas) < sum(cost):
            return -1
        i = 0
        while i < n:
            if cost[i] > gas[i]:
                i += 1
                continue
            ret = gas[i] - cost[i]
            j = i + 1 if i < n - 1 else 0
            while j != i:
                ret += gas[j] - cost[j]
                if ret < 0:
                    break
                if j == n - 1:
                    j = 0
                else:
                    j += 1
            if j == i and ret >= 0:
                return i
            else:
                i = j + 1

        return -1


def test():
    assert Solution().canCompleteCircuit(gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2]) == 3
    assert Solution().canCompleteCircuit(gas=[2, 3, 4], cost=[3, 4, 3]) == -1
    assert Solution().canCompleteCircuit(gas=[4], cost=[5]) == -1
    assert Solution().canCompleteCircuit(gas=[5], cost=[5]) == 0


if __name__ == '__main__':
    test()
