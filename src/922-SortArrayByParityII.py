#!/usr/bin/env python
"""
CREATED AT: 2021/9/28
Des:

https://leetcode.com/problems/sort-array-by-parity-ii
https://leetcode.com/explore/item/3990
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy
"""
from typing import List

from tool import print_results


class Solution:
    @print_results
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        """
        61 / 61 test cases passed.
        Status: Accepted
        Runtime: 220 ms
        Memory Usage: 16.2 MB
        :param nums:
        :return:
        """
        j = 1
        for i in range(0, len(nums), 2):
            if nums[i] % 2 == 0:
                continue
            while j < len(nums) and nums[j] % 2 == 1:
                j += 2
            nums[i], nums[j] = nums[j], nums[i]
        return nums


def test():
    ans = [[4, 5, 2, 7], [2, 5, 4, 7], [2, 7, 4, 5]]
    assert Solution().sortArrayByParityII(nums=[4, 2, 5, 7]) in ans

    assert Solution().sortArrayByParityII(nums=[2, 3]) == [2, 3]
    assert Solution().sortArrayByParityII(nums=[2, 3, 1, 1, 4, 0, 0, 4, 3, 3])


if __name__ == '__main__':
    test()
