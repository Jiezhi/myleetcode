#!/usr/bin/env python
"""
CREATED AT: 2021/9/6
Des:
https://leetcode.com/problems/sort-colors/
https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/798/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium
"""
import collections
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt = collections.Counter(nums)
        cur = 0
        for i in range(len(nums)):
            while not cnt[cur]:
                cur += 1
            nums[i] = cur
            cnt[cur] -= 1

    def sortColors2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        87 / 87 test cases passed.
        Status: Accepted
        Runtime: 32 ms
        Memory Usage: 13.9 MB
        """
        cnt = collections.Counter(nums)

        cnt_0 = cnt.get(0)
        if cnt_0 is None:
            cnt_0 = 0
        cnt_1 = cnt.get(1)
        if cnt_1 is None:
            cnt_1 = 0
        for i in range(len(nums)):
            if i < cnt_0:
                nums[i] = 0
            elif i < cnt_0 + cnt_1:
                nums[i] = 1
            else:
                nums[i] = 2


def test():
    nums = [2, 0, 2, 1, 1, 0]
    Solution().sortColors(nums=nums)
    assert nums == [0, 0, 1, 1, 2, 2]

    nums = [0]
    Solution().sortColors(nums=nums)
    assert nums == [0]

    nums = [1]
    Solution().sortColors(nums=nums)
    assert nums == [1]

    nums = [2, 0, 1]
    Solution().sortColors(nums=nums)
    assert nums == [0, 1, 2]


if __name__ == '__main__':
    test()
