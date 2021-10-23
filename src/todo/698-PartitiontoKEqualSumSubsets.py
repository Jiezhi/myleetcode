#!/usr/bin/env python
"""
CREATED AT: 2021/9/30
Des:
https://leetcode.com/problems/partition-to-k-equal-sum-subsets
https://leetcode.com/explore/item/3993
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: 
"""
from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if k == 1:
            return True
        nums = sorted(nums, reverse=True)
        n, l = divmod(sum(nums), k)
        if l != 0 or nums[0] > n:
            return False
        rets = [0 for _ in range(k)]
        for num in nums:
            if num > n:
                return False
            found = False
            for i in range(k):
                if rets[i] + num <= n:
                    rets[i] += num
                    found = True
                    break
            if not found:
                return False
        return True


def test():
    assert Solution().canPartitionKSubsets(
        [3522, 181, 521, 515, 304, 123, 2512, 312, 922, 407, 146, 1932, 4037, 2646, 3871, 269], 5)
    assert Solution().canPartitionKSubsets(nums=[4, 3, 2, 3, 5, 2, 1], k=4)
    assert not Solution().canPartitionKSubsets(nums=[1, 2, 3, 4], k=3)
    assert Solution().canPartitionKSubsets(nums=[1, 2, 3], k=2)
    assert not Solution().canPartitionKSubsets(nums=[1, 2, 3], k=3)


if __name__ == '__main__':
    test()
