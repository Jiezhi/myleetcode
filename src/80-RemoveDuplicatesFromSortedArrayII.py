#!/usr/bin/env python
"""
CREATED AT: 2022/2/6
Des:

https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

Time Spent:  min
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        CREATED AT: 2022/2/11
        Runtime: 60 ms, faster than 76.15%
        Memory Usage: 13.9 MB, less than 46.45%
        1 <= nums.length <= 3 * 10^4
        -10^4 <= nums[i] <= 10^4
        nums is sorted in non-decreasing order.
        :param nums:
        :return:
        """
        n = len(nums)
        if n <= 2:
            return n
        dup = 0
        h1, h2 = nums[0], nums[1]
        for i in range(2, n):
            while i + dup < n and h1 == h2 and h2 == nums[i + dup]:
                dup += 1
            if i + dup >= n:
                break
            nums[i] = nums[i + dup]
            h1, h2 = nums[i - 1], nums[i]

        return n - dup


def test():
    nums = [2, 2, 2, 1, 1, 1, 1, 3, 3, 3, 3, 3]
    ans = [2, 2, 1, 1, 3, 3]
    ret = Solution().removeDuplicates(nums=nums)
    assert nums[:ret] == ans

    nums = [1, 1, 1, 2, 2, 3]
    ans = [1, 1, 2, 2, 3]
    ret = Solution().removeDuplicates(nums=nums)
    assert nums[:ret] == ans

    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    ans = [0, 0, 1, 1, 2, 3, 3]
    ret = Solution().removeDuplicates(nums=nums)
    assert nums[:ret] == ans


if __name__ == '__main__':
    test()
