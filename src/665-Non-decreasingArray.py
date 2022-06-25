#!/usr/bin/env python3
"""
CREATED AT: 2022-06-25

URL: https://leetcode.com/problems/non-decreasing-array/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 665-Non-decreasingArray

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        """
        Runtime: 323 ms, faster than 30.11%
        Memory Usage: 15.3 MB, less than 15.99%

        n == nums.length
        1 <= n <= 10^4
        -10^5 <= nums[i] <= 10^5
        """

        def isDecrease(nums) -> bool:
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    return False
            return True

        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if i == 0:
                    return isDecrease(nums[1:])
                else:
                    # change nums[i] to nums[i - 1] or chnage nums[i + 1] to nums[i]
                    return isDecrease([nums[i - 1]] + nums[i + 1:]) or isDecrease([nums[i]] + nums[i + 2:])
        return True


def test():
    assert Solution().checkPossibility(nums=[4, 2, 3])
    assert not Solution().checkPossibility(nums=[4, 2, 1])


if __name__ == '__main__':
    test()
