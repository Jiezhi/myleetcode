#!/usr/bin/env python
"""
CREATED AT: 2022/3/15
Des:
https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""
from typing import List


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        """
        Runtime: 252 ms, faster than 70.61%
        Memory Usage: 17.6 MB, less than 16.36%

        1 <= nums.length <= 16
        1 <= nums[i] <= 10^5
        """
        ret = []
        for num in nums:
            tmp_ret = ret.copy()
            for r in tmp_ret:
                ret.append(num | r)
            ret.append(num)
        ret = sorted(ret, reverse=True)
        max_value = ret[0]
        cnt = 1
        for v in ret[1:]:
            if v == max_value:
                cnt += 1
            else:
                break
        return cnt


def test():
    assert Solution().countMaxOrSubsets(nums=[3, 1]) == 2
    assert Solution().countMaxOrSubsets(nums=[2, 2, 2]) == 7
    assert Solution().countMaxOrSubsets(nums=[3, 2, 1, 5]) == 6


if __name__ == '__main__':
    test()
