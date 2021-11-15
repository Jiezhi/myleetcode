#!/usr/bin/env python
"""
CREATED AT: 2021/11/15
Des:

https://leetcode.com/problems/largest-divisible-subset/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 
"""
from typing import List


class Solution:

    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        """
        Runtime: 2796 ms, faster than 5.00%
        Memory Usage: 14.7 MB, less than 23.50%
        1 <= nums.length <= 1000
        1 <= nums[i] <= 2 * 10^9
        All the integers in nums are unique.
        :param nums:
        :return:
        """
        nums = sorted(nums)
        rets = [[nums[0]]]
        for num in nums[1:]:
            tmp_rets = []
            for ret in rets:
                index = -1
                for i in range(len(ret)):
                    if num % ret[i] != 0:
                        index = i
                        break
                if index == -1:
                    ret.append(num)
                else:
                    tmp_ret = ret[:index]
                    tmp_ret.append(num)
                    tmp_rets.append(tmp_ret)
            ret = [num]
            for tmp_ret in tmp_rets:
                if len(tmp_ret) > len(ret):
                    ret = tmp_ret
            rets.append(ret)
        ret = rets[0]
        for r in rets[1:]:
            if len(r) > len(ret):
                ret = r
        return ret


def test():
    ret = Solution().largestDivisibleSubset(nums=list(range(1, 1001)))
    print(ret)
    ret = Solution().largestDivisibleSubset(nums=[1, 2, 3])
    assert ret == [1, 2] or ret == [1, 3]
    assert Solution().largestDivisibleSubset(nums=[1, 2, 4, 8]) == [1, 2, 4, 8]


if __name__ == '__main__':
    test()
