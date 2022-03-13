#!/usr/bin/env python
"""
CREATED AT: 2022/3/13
Des:

https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

"""
from typing import List


class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        """
        1 <= nums.length <= 1000
        1 <= nums[i] <= 1000
        key is an integer from the array nums.
        1 <= k <= nums.length
        """
        key_pos = []
        for i in range(len(nums)):
            if nums[i] == key:
                key_pos.append(i)

        ret = set()
        for pos in key_pos:
            for r in range(max(0, pos - k), min(len(nums), pos + k + 1)):
                ret.add(r)

        return sorted(list(ret))


def test():
    assert Solution().findKDistantIndices(nums=[3, 4, 9, 1, 3, 9, 5], key=9, k=1) == [1, 2, 3, 4, 5, 6]
    assert Solution().findKDistantIndices(nums=[2, 2, 2, 2, 2], key=2, k=2) == [0, 1, 2, 3, 4]


if __name__ == '__main__':
    test()
