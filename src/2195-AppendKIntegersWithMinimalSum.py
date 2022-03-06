#!/usr/bin/env python
"""
CREATED AT: 2022/3/6
Des:

https://leetcode.com/problems/append-k-integers-with-minimal-sum/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

Time Spent:  min
"""
from typing import List


class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        """
        1 <= nums.length <= 10^5
        1 <= nums[i], k <= 10^9
        """
        # total_sum = sum(range(k + 1))
        total_sum = k * (k + 1) // 2
        next_sum = k + 1
        nums = sorted(nums)
        pre_num = nums[0] - 1
        for num in nums:
            if num == pre_num:
                continue
            pre_num = num
            if num < next_sum:
                total_sum = total_sum - num + next_sum
                next_sum += 1
            else:
                break
        return total_sum


def test():
    assert Solution().minimalKSum(nums=[1, 4, 25, 10, 25], k=2) == 5
    assert Solution().minimalKSum(nums=[5, 6], k=6) == 25


if __name__ == '__main__':
    test()
