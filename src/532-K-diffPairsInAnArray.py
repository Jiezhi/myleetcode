#!/usr/bin/env python
"""
CREATED AT: 2022/2/9
Des:

https://leetcode.com/problems/k-diff-pairs-in-an-array/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

Time Spent:  min
"""
from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        """
        CREATED AT: 2022/2/9
        Runtime: 752 ms, faster than 5.67%
        Memory Usage: 15.4 MB, less than 90.40%
        1 <= nums.length <= 10^4
        -10^7 <= nums[i] <= 10^7
        0 <= k <= 10^7
        :param nums:
        :param k:
        :return:
        """

        def bs(arr, x) -> bool:
            if not arr or x < arr[0] or x > arr[-1]:
                return False
            lo, hi = 0, len(arr) - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if arr[mid] == x:
                    return True
                elif arr[mid] < x:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return False

        nums = sorted(nums)
        last = nums[0] - 1
        ret = 0
        for i in range(len(nums)):
            if nums[i] == last:
                continue
            if nums[i] + k > nums[-1]:
                break
            if bs(nums[i + 1:], nums[i] + k):
                ret += 1
            last = nums[i]
        return ret


def test():
    assert Solution().findPairs(nums=[3, 1, 4, 1, 5], k=2) == 2
    assert Solution().findPairs(nums=[1, 2, 3, 4, 5], k=1) == 4
    assert Solution().findPairs(nums=[1, 3, 1, 5, 4], k=0) == 1


if __name__ == '__main__':
    test()
