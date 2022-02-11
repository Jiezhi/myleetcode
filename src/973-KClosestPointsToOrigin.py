#!/usr/bin/env python
"""
CREATED AT: 2022/2/11
Des:

https://leetcode.com/problems/k-closest-points-to-origin
https://leetcode.com/explore/item/4088
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

Time Spent:  min
"""
import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        CREATED AT: 2022/2/11
        87 / 87 test cases passed.
        Status: Accepted
        Runtime: 801 ms, faster than 57.77%
        Memory Usage: 20.3 MB, less than 39.34%
        1 <= k <= points.length <= 10^4
        -10^4 < xi, yi < 10^4
        """
        if k == len(points):
            return points

        heap = [(-(x[0] * x[0] + x[1] * x[1]), x) for x in points[:k]]
        heapq.heapify(heap)

        for p in points[k:]:
            dist = -(p[0] * p[0] + p[1] * p[1])
            if dist > heap[0][0]:
                heapq.heapreplace(heap, (dist, p))

        return [x[1] for x in heap]


def test():
    assert Solution().kClosest([[1, 3], [-2, 2]], 1) == [[-2, 2]]
    assert Solution().kClosest(points=[[3, 3], [5, -1], [-2, 4]], k=2) in [[[3, 3], [-2, 4]], [[-2, 4], [3, 3]]]


if __name__ == '__main__':
    test()
