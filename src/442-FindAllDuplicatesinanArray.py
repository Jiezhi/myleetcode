#!/usr/bin/env python
"""
CREATED AT: 2021/10/6
Des:

https://leetcode.com/problems/find-all-duplicates-in-an-array

GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Reference: https://leetcode.com/problems/find-all-duplicates-in-an-array/discuss/92387/Java-Simple-Solution
"""
from typing import List

from tool import equal_list_value


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        """
        28 / 28 test cases passed.
        Status: Accepted
        Runtime: 372 ms
        Memory Usage: 21.6 MB
        :param nums:
        :return:
        """
        ret = []
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] < 0:
                ret.append(abs(nums[i]))
            nums[index] = -nums[index]
        return ret


def test():
    assert equal_list_value(Solution().findDuplicates(nums=[4, 3, 2, 7, 8, 2, 3, 1]), [2, 3])
    assert equal_list_value(Solution().findDuplicates(nums=[10, 2, 5, 10, 9, 1, 1, 4, 3, 7]), [10, 1])
    assert Solution().findDuplicates(nums=[1, 1, 2]) == [1]
    assert Solution().findDuplicates(nums=[1]) == []


if __name__ == '__main__':
    test()
