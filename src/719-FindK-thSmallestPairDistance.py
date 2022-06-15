#!/usr/bin/env python3
"""
CREATED AT: 2022-06-15

URL: https://leetcode.com/problems/find-k-th-smallest-pair-distance/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 719-FindK-thSmallestPairDistance

Difficulty: Hard

Desc: 

Tag: BS

See: https://leetcode.cn/problems/find-k-th-smallest-pair-distance/solution/zhao-chu-di-k-xiao-de-shu-dui-ju-chi-by-xwfgf/

"""
import bisect
from typing import List


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        """
        Runtime: 205 ms, faster than 43.50%
        Memory Usage: 14.9 MB, less than 52.17%
        n == nums.length
        2 <= n <= 10^4
        0 <= nums[i] <= 10^6
        1 <= k <= n * (n - 1) / 2
        """
        nums = sorted(nums)

        def count(mid: int) -> int:
            ret = 0
            for j, num in enumerate(nums):
                ret += j - bisect.bisect_left(nums, num - mid, 0, j)
            return ret

        # for py 10: return bisect.bisect_left(range(nums[-1] - nums[0]), k, key=count)

        i, j = 0, nums[-1] - nums[0]
        while i < j:
            mid = (i + j) // 2
            r = count(mid)
            if r >= k:
                j = mid
            else:
                i = mid + 1
        return i


def test():
    assert Solution().smallestDistancePair(nums=[1, 3, 1], k=1) == 0
    assert Solution().smallestDistancePair(nums=[1, 6, 1], k=3) == 5


if __name__ == '__main__':
    test()
