#!/usr/bin/env python
"""
CREATED AT: 2022/4/25
Des:
https://leetcode.com/problems/random-pick-index/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""
import collections
import random
from typing import List


class Solution:
    """
    Runtime: 440 ms, faster than 34.43%
    Memory Usage: 24.3 MB, less than 13.02%
    1 <= nums.length <= 2 * 10^4
    -2^31 <= nums[i] <= 2^31 - 1
    target is an integer from nums.
    At most 10^4 calls will be made to pick.
    """

    def __init__(self, nums: List[int]):
        self.dct = collections.defaultdict(list)
        for i, num in enumerate(nums):
            self.dct[num].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.dct[target])


def test():
    nums = [1, 2, 3, 3, 3]
    s = Solution(nums)
    for i in range(10):
        assert s.pick(3) in [2, 3, 4]


if __name__ == '__main__':
    test()
