#!/usr/bin/env python
"""
CREATED AT: 2022/3/13
Des:

GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""
from typing import List


class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        """
        1 <= nums.length <= 10^5
        0 <= nums[i], k <= 10^9
        """
        if len(nums) == 1:
            return -1 if k % 2 == 1 else nums[0]
        if k == 0:
            return nums[0]
        if k == 1:
            return nums[1]
        n = len(nums)
        if k > n:
            return max(nums)
        elif k == n:
            return max(nums[:k - 1])
        else:
            # k < n
            return max(max(nums[:k - 1]), nums[k])


def test():
    assert Solution().maximumTop(nums=[5, 2, 2, 4, 0, 6], k=4) == 5
    assert Solution().maximumTop(nums=[2], k=1) == -1


if __name__ == '__main__':
    test()
