#!/usr/bin/env python3
"""
CREATED AT: 2022-08-29

URL: https://leetcode.com/problems/shuffle-the-array/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1470-ShuffleTheArray

Difficulty: Easy

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        """
        Runtime: 96 ms, faster than 50.97%
        Memory Usage: 14.2 MB, less than 41.17%

        1 <= n <= 500
        nums.length == 2n
        1 <= nums[i] <= 10^3
        """
        ret = []
        for i in range(n):
            ret.append(nums[i])
            ret.append(nums[i + n])
        return ret


def test():
    assert Solution().shuffle(nums=[2, 5, 1, 3, 4, 7], n=3) == [2, 3, 5, 4, 1, 7]
    assert Solution().shuffle(nums=[1, 2, 3, 4, 4, 3, 2, 1], n=4) == [1, 4, 2, 3, 3, 2, 4, 1]
    assert Solution().shuffle(nums=[1, 1, 2, 2], n=2) == [1, 2, 1, 2]


if __name__ == '__main__':
    test()
