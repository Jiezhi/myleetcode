#!/usr/bin/env python
"""
CREATED AT: 2021/9/28
Des:
https://leetcode.com/problems/maximum-sum-circular-subarray/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tags: DP

See: 53
"""
from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        max_ret_here = max_ret = nums[0]
        current_len = max_curr_len = 1
        nums = nums + nums
        for i, x in enumerate(nums[1:], start=1):
            if current_len == n:
                # reach the max length
                if x >= x + max_ret_here - nums[i - n]:
                    max_ret_here = x
                    current_len = 1
                else:
                    max_ret_here = max_ret_here + x - nums[i - n]
            else:
                if x > x + max_ret_here:
                    max_ret_here = x
                    current_len = 1
                else:
                    max_ret_here += x
                    current_len += 1

            if max_ret_here > max_ret:
                max_ret = max_ret_here
            #     max_curr_len = current_len
            # else:
            #     current_len = max_curr_len
        return max_ret


def test():
    # assert Solution().maxSubarraySumCircular(nums=[1, -2, 3, -2]) == 3
    assert Solution().maxSubarraySumCircular(nums=[5, -3, 5]) == 10
    assert Solution().maxSubarraySumCircular(nums=[3, -1, 2, -1]) == 4
    assert Solution().maxSubarraySumCircular(nums=[3, 1, 2, -1, 4]) == 10


if __name__ == '__main__':
    test()
