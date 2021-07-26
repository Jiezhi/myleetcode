#!/usr/bin/env python
"""
CREATED AT: 2021/7/26
Des:

https://leetcode.com/problems/contains-duplicate/
https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/578/
GITHUB: https://github.com/Jiezhi/myleetcode

"""
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


def test():
    assert Solution().containsDuplicate(nums=[1, 2, 3, 1])
    assert not Solution().containsDuplicate(nums=[1, 2, 3, 4])


if __name__ == '__main__':
    test()
