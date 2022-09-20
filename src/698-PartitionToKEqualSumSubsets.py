#!/usr/bin/env python3
"""
CREATED AT: 2022-09-20

URL: https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
https://leetcode.com/explore/item/3993

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 698-PartitionToKEqualSumSubsets

Difficulty: Medium

Desc: 

Tag: 

See: https://leetcode.cn/problems/partition-to-k-equal-sum-subsets/solution/hua-fen-wei-kge-xiang-deng-de-zi-ji-by-l-v66o/

"""
from tool import *


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        """
        Runtime: 1220 ms, faster than 26.23%
        Memory Usage: 33.3 MB, less than 29.58%

        https://leetcode.cn/problems/partition-to-k-equal-sum-subsets/solution/hua-fen-wei-kge-xiang-deng-de-zi-ji-by-l-v66o/

        1 <= k <= nums.length <= 16
        1 <= nums[i] <= 10^4
        The frequency of each element is in the range [1, 4].
        """
        per, l = divmod(sum(nums), k)
        if l:
            return False
        n = len(nums)
        nums.sort()
        if nums[-1] > per:
            return False

        @cache
        def dp(state, cur) -> bool:
            if state == 0:
                return True
            for i in range(n):
                if cur + nums[i] > per:
                    break
                if (state >> i) & 1 and dp(state ^ (1 << i), (cur + nums[i]) % per):
                    return True
            return False

        return dp((1 << n) - 1, 0)


def test():
    assert Solution().canPartitionKSubsets(nums=list(range(1, 17)), k=8)
    assert Solution().canPartitionKSubsets(nums=[1, 1, 1, 1, 2, 2, 2, 2], k=3)
    assert Solution().canPartitionKSubsets(nums=[4, 3, 2, 3, 5, 2, 1], k=4)
    assert not Solution().canPartitionKSubsets(nums=[1, 2, 3, 4], k=3)


if __name__ == '__main__':
    test()
