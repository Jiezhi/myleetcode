#!/usr/bin/env python
"""
CREATED AT: 2022/2/10
Des:

https://leetcode.com/problems/subarray-sum-equals-k/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

Time Spent:  min
"""
import collections
from typing import List


class Solution:
    def subarraySum2(self, nums: List[int], k: int) -> int:
        """
        CREATED AT: 2022/2/10
        Runtime: 324 ms, faster than 51.18%
        Memory Usage: 18.5 MB, less than 8.13%

        Solved by hints
        1 <= nums.length <= 2 * 10^4
        -1000 <= nums[i] <= 1000
        -10^7 <= k <= 10^7
        :param nums:
        :param k:
        :return:
        """
        ret = 0

        acc_sum = [nums[0]]
        sum_map = collections.defaultdict(int)
        sum_map[nums[0]] += 1

        for num in nums[1:]:
            acc_sum.append(acc_sum[-1] + num)
            sum_map[acc_sum[-1]] += 1

        ret += sum_map[k]

        for s in acc_sum:
            sum_map[s] -= 1
            ret += sum_map[k + s]
        return ret

    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        CREATED AT: 2022/2/10
        Runtime: 370 ms, faster than 40.31%
        Memory Usage: 18.3 MB, less than 16.42%
        1 <= nums.length <= 2 * 10^4
        -1000 <= nums[i] <= 1000
        -10^7 <= k <= 10^7
        :param nums:
        :param k:
        :return:
        """
        ret = 0
        d = collections.defaultdict(int)
        d[0] = 1
        acc_sum = 0
        for num in nums:
            acc_sum += num
            ret += d[acc_sum - k]
            d[acc_sum] += 1
        return ret


def test():
    assert Solution().subarraySum(nums=[-1, -1, 1], k=0) == 1
    assert Solution().subarraySum(nums=[1], k=0) == 0
    assert Solution().subarraySum(nums=[1, 2, 1, 2], k=3) == 3
    assert Solution().subarraySum(nums=[2], k=2) == 1
    assert Solution().subarraySum(nums=[1, 1, 1], k=2) == 2
    assert Solution().subarraySum(nums=[1, 2, 3], k=3) == 2
    assert Solution().subarraySum(nums=[1, -1, 1, 2, 3], k=3) == 3


if __name__ == '__main__':
    test()
