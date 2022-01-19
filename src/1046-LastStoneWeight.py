#!/usr/bin/env python
"""
CREATED AT: 2022/1/19
Des:

https://leetcode.com/problems/last-stone-weight/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

Time Spent:  min
"""
import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        70 / 70 test cases passed.
        Status: Accepted
        Runtime: 24 ms
        Memory Usage: 14.4 MB

        1 <= stones.length <= 30
        1 <= stones[i] <= 1000
        :param stones:
        :return:
        """
        if len(stones) == 1:
            return stones[0]
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            k1 = heapq.heappop(stones)
            k2 = heapq.heappop(stones)
            if k1 != k2:
                heapq.heappush(stones, k1 - k2)
        if len(stones) == 1:
            return -stones[0]
        else:
            return 0


def test():
    assert Solution().lastStoneWeight(stones=[2, 7, 4, 1, 8, 1]) == 1
    assert Solution().lastStoneWeight(stones=[1]) == 1


if __name__ == '__main__':
    test()
