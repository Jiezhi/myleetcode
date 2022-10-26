#!/usr/bin/env python3
"""
CREATED AT: 2022-10-26

URL: https://leetcode.com/problems/continuous-subarray-sum/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 523-ContinuousSubarraySum

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """
        inspired by: https://leetcode.com/problems/continuous-subarray-sum/solution/
        Runtime: 2787 ms, faster than 10.88%
        Memory Usage: 29.4 MB, less than 95.95%

        1 <= nums.length <= 10^5
        0 <= nums[i] <= 10^9
        0 <= sum(nums[i]) <= 2^31 - 1
        1 <= k <= 2^31 - 1
        """
        acc = list(itertools.accumulate([0] + nums, lambda a, b: (a + b) % k))
        pre = set()
        for i in range(len(nums) - 1):
            pre.add(acc[i])
            if acc[i + 2] % k in pre:
                return True
        return False


def test():
    assert Solution().checkSubarraySum(nums=[23, 2, 4, 6, 7], k=6)
    assert Solution().checkSubarraySum(nums=[23, 2, 6, 4, 7], k=6)
    assert not Solution().checkSubarraySum(nums=[23, 2, 6, 4, 7], k=13)


if __name__ == '__main__':
    test()
