#!/usr/bin/env python
"""
CREATED AT: 2022/2/21
Des:

GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Hard

Tag: 

See: 

Time Spent:  min
"""
import collections
import math
from typing import List


class Solution:
    def coutPairs(self, nums: List[int], k: int) -> int:
        """
        Ref: https://leetcode.com/problems/count-array-pairs-divisible-by-k/discuss/1785027/C%2B%2BPython-Easy-and-Concise-with-Explanation
        Runtime: 1183 ms, faster than 100.00%
        Memory Usage: 28.1 MB, less than 33.33%
        1 <= nums.length <= 10^5
        1 <= nums[i], k <= 10^5
        """
        gcd_cnts = collections.Counter(math.gcd(x, k) for x in nums)
        ret = 0
        for i in gcd_cnts:
            for j in gcd_cnts:
                if i <= j and i * j % k == 0:
                    if i < j:
                        ret += gcd_cnts[i] * gcd_cnts[j]
                    else:
                        ret += gcd_cnts[i] * (gcd_cnts[i] - 1) // 2
        return ret


def test():
    assert Solution().coutPairs(nums=[1, 2, 3, 4, 5], k=2) == 7
    assert Solution().coutPairs(nums=[1, 2, 3, 4], k=5) == 0


if __name__ == '__main__':
    test()
