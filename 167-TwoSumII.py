#!/usr/bin/env python
"""
Github: https://github.com/Jiezhi/myleetcode

Created on 2019/8/28

Leetcode: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

"""
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            if (target - numbers[i]) in numbers:
                return [i + 1, numbers.index(target - numbers[i], i + 1) + 1]


def test():
    assert Solution().twoSum([2, 7, 11, 15], 9) == [1, 2]
    assert Solution().twoSum([0, 0, 3, 4], 0) == [1, 2]


if __name__ == '__main__':
    test()
