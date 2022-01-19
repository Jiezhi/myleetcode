#!/usr/bin/env python
"""
CREATED AT: 2022/1/19
Des:

GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

Time Spent:  min
"""
import heapq
from typing import List


class KthLargest:
    """
    10 / 10 test cases passed.
    Status: Accepted
    Runtime: 162 ms
    Memory Usage: 18.3 MB

    1 <= k <= 10^4
    0 <= nums.length <= 10^4
    -10^4 <= nums[i] <= 10^4
    -10^4 <= val <= 10^4
    At most 10^4 calls will be made to add.
    It is guaranteed that there will be at least k elements in the array when you search for the kth element.
    """

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)
        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val)
        elif val > self.nums[0]:
            heapq.heapreplace(self.nums, val)
        return self.nums[0]


def test():
    solution = KthLargest(k=1, nums=[])
    assert solution.add(-3) == -3

    solution = KthLargest(k=3, nums=[4, 5, 8, 2])
    assert solution.add(3) == 4
    assert solution.add(5) == 5
    assert solution.add(10) == 5
    assert solution.add(9) == 8
    assert solution.add(4) == 8


if __name__ == '__main__':
    test()
