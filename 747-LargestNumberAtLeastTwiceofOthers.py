#!/usr/bin/env python
"""
Github: https://github.com/Jiezhi/myleetcode

Created on 2019-08-15

Leetcode: https://leetcode.com/problems/largest-number-at-least-twice-of-others/

"""
from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        tmp_i = -1
        tmp_max = -1
        for i, num in enumerate(nums):
            if tmp_max >= num * 2:
                continue
            elif tmp_max < num:
                if tmp_max * 2 <= num:
                    tmp_i = i
                else:
                    tmp_i = -1
                tmp_max = num
            else:
                tmp_i = -1
        return tmp_i

    def dominantIndex2(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        max_1 = max(nums)
        max_i = nums.index(max_1)
        nums.remove(max_1)
        max_2 = max(nums)
        if max_1 >= max_2 * 2:
            return max_i
        else:
            return -1


def test():
    assert Solution().dominantIndex([6]) == 0
    assert Solution().dominantIndex([3, 6, 1, 0]) == 1
    assert Solution().dominantIndex([1, 2, 3, 4]) == -1

    assert Solution().dominantIndex2([6]) == 0
    assert Solution().dominantIndex2([3, 6, 1, 0]) == 1
    assert Solution().dominantIndex2([1, 2, 3, 4]) == -1


if __name__ == '__main__':
    test()
