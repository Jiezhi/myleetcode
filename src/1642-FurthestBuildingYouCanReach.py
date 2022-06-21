#!/usr/bin/env python3
"""
CREATED AT: 2022-06-21

URL: https://leetcode.com/problems/furthest-building-you-can-reach/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1642-FurthestBuildingYouCanReach

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
import heapq
from typing import List


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        """
        Runtime: 1069 ms, faster than 23.29%
        Memory Usage: 28.5 MB, less than 54.37%
        1 <= heights.length <= 10^5
        1 <= heights[i] <= 10^6
        0 <= bricks <= 10^9
        0 <= ladders <= heights.length
        """
        acc = 0
        heap = []
        for i, h in enumerate(heights[1:], 1):
            diff = h - heights[i - 1]
            if diff > 0:
                if len(heap) >= ladders:
                    acc += heapq.heappushpop(heap, diff)
                    if acc > bricks:
                        return i - 1
                else:
                    heapq.heappush(heap, diff)

        return len(heights) - 1


def test():
    assert Solution().furthestBuilding(heights=[4, 2, 7, 6, 9, 14, 12], bricks=5, ladders=1) == 4
    assert Solution().furthestBuilding(heights=[4, 12, 2, 7, 3, 18, 20, 3, 19], bricks=10, ladders=2) == 7
    assert Solution().furthestBuilding(heights=[14, 3, 19, 3], bricks=17, ladders=0) == 3


if __name__ == '__main__':
    test()
