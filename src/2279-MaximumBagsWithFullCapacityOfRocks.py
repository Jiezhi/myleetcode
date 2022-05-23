#!/usr/bin/env python
"""
CREATED AT: 2022/5/23
Des:
https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""
from typing import List


class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        """
        79 / 79 test cases passed.
        Status: Accepted 05/23/2022
        Runtime: 1536 ms
        Memory Usage: 22 MB
        :param capacity:
        :param rocks:
        :param additionalRocks:
        n == capacity.length == rocks.length
        1 <= n <= 5 * 10^4
        1 <= capacity[i] <= 10^9
        0 <= rocks[i] <= capacity[i]
        1 <= additionalRocks <= 10^9
        :return:
        """
        leftover = sorted([capacity[i] - rocks[i] for i in range(len(rocks))])
        i = 0
        while additionalRocks > 0 and i < len(leftover):
            if leftover[i] > additionalRocks:
                break
            additionalRocks -= leftover[i]
            i += 1
        return i if i <= len(leftover) else i - 1


def test():
    assert Solution().maximumBags(capacity=[2, 3, 4, 5], rocks=[1, 2, 4, 4], additionalRocks=2) == 3


if __name__ == '__main__':
    test()
