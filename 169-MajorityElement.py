#!/usr/bin/env python
"""
CREATED AT: 2021/9/12
Des:
https://leetcode.com/problems/majority-element/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Reference: https://leetcode.com/problems/majority-element/solution/
"""
import collections
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        47 / 47 test cases passed.
        Status: Accepted
        Runtime: 214 ms
        Memory Usage: 15.6 MB
        :param nums:
        :return:
        """
        return collections.Counter(nums).most_common(1)[0][0]

    def majorityElement2(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums) // 2]


def test():
    assert Solution().majorityElement(nums=[3, 2, 3]) == 3
    assert Solution().majorityElement2(nums=[3, 2, 3]) == 3


if __name__ == '__main__':
    test()
