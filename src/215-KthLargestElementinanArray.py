#!/usr/bin/env python
"""
CREATED AT: 2021/9/7
Updated at 2022/01/19
Des:
https://leetcode.com/problems/kth-largest-element-in-an-array/
https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/800/
https://leetcode.com/explore/featured/card/heap/646/practices/4014/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: heap
"""
import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Updated at 2022/01/19
        32 / 32 test cases passed.
        Status: Accepted
        Runtime: 124 ms
        Memory Usage: 15.2 MB

        1 <= k <= nums.length <= 10^4
        -10^4 <= nums[i] <= 10^4
        :param nums:
        :param k:
        :return:
        """
        max_value = 10 ** 4
        nums = [max_value - x for x in nums]
        heapq.heapify(nums)
        i = 1
        while i < k:
            heapq.heappop(nums)
            i += 1
        return max_value - nums[0]

    def findKthLargest2(self, nums: List[int], k: int) -> int:
        """
        32 / 32 test cases passed.
        Status: Accepted
        Runtime: 90 ms
        Memory Usage: 15.1 MB
        :param nums:
        :param k:
        :return:
        """
        return sorted(nums, reverse=True)[k - 1]


def test():
    assert Solution().findKthLargest(nums=[3, 2, 1, 5, 6, 4], k=2) == 5
    assert Solution().findKthLargest(nums=[3, 2, 3, 1, 2, 4, 5, 5, 6], k=4) == 4
    assert Solution().findKthLargest(nums=[-5, -10, 8, 7, 10, 200, 400, -900], k=2) == 200


if __name__ == '__main__':
    test()
