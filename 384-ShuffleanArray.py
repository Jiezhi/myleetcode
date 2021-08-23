#!/usr/bin/env python
"""
CREATED AT: 2021/8/23
Des:

https://leetcode.com/problems/shuffle-an-array/
https://leetcode.com/explore/featured/card/top-interview-questions-easy/98/design/670/
GITHUB: https://github.com/Jiezhi/myleetcode

"""
import random
from typing import List

from itertools import permutations, cycle


class Solution2:
    """
    sample 196 ms submission
    """

    def __init__(self, nums: List[int]):
        self.reset = lambda: nums
        c = cycle(permutations(nums))
        self.shuffle = lambda: list(next(c))


class Solution:
    """
    10 / 10 test cases passed.
    Status: Accepted
    Runtime: 264 ms
    Memory Usage: 19.5 MB
    """

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.copy = self.nums.copy()

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.nums = self.copy.copy()
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        random.shuffle(self.nums)
        return self.nums


def test():
    nums = [1, 2, 3]
    solution = Solution(nums=nums)
    assert solution.reset() == nums
    ret = solution.shuffle()
    assert len(ret) == len(ret)
    for i in nums:
        assert i in ret
    assert solution.reset() == nums


if __name__ == '__main__':
    test()
