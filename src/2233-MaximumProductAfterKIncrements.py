#!/usr/bin/env python
"""
CREATED AT: 2022/4/10
Des:
https://leetcode.com/problems/maximum-product-after-k-increments/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""
import heapq
from typing import List


class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        """
        1 <= nums.length, k <= 10^5
        0 <= nums[i] <= 10^6
        :param nums:
        :param k:
        :return:
        """
        if len(nums) == 1:
            return nums[0] + k
        M = 10 ** 9 + 7
        heapq.heapify(nums)
        while k > 0:
            n1 = heapq.heappop(nums)
            diff = min(nums[0] - n1 + 1, k)
            heapq.heappush(nums, n1 + diff)
            k -= diff
        ret = 1
        for n in nums:
            ret *= n
            ret %= M
        return ret


def test():
    assert Solution().maximumProduct(nums=[0, 4], k=5) == 20
    assert Solution().maximumProduct(nums=[6, 3, 3, 2], k=2) == 216


if __name__ == '__main__':
    test()
