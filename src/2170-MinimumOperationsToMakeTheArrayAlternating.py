#!/usr/bin/env python
"""
CREATED AT: 2022/2/13
Des:

https://leetcode.com/problems/minimum-operations-to-make-the-array-alternating/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: 

Tag: 

See: 

Time Spent: 17 min
"""
import collections
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        """
        Runtime: 1484 ms, faster than 75.00%
        Memory Usage: 30.2 MB, less than 87.50%
        1 <= nums.length <= 10^5
        1 <= nums[i] <= 10^5
        """
        n = len(nums)
        if n <= 1:
            return 0
        odd_len = n // 2
        even_len = n - odd_len

        cnt1 = collections.Counter(nums[x] for x in range(0, n, 2))
        cnt2 = collections.Counter(nums[x] for x in range(1, n, 2))
        most1 = cnt1.most_common(2)
        most2 = cnt2.most_common(2)
        if most1[0][0] != most2[0][0]:
            return (even_len - most1[0][1]) + (odd_len - most2[0][1])
        else:
            if len(most1) < 2 and len(most2) < 2:
                return odd_len
            if len(most1) < 2:
                return (even_len - most1[0][1]) + (odd_len - most2[1][1])
            elif len(most2) < 2:
                return (even_len - most1[1][1]) + (odd_len - most2[0][1])
            return min((even_len - most1[0][1]) + (odd_len - most2[1][1]),
                       (even_len - most1[1][1]) + (odd_len - most2[0][1]))


def test():
    assert Solution().minimumOperations(nums=[3, 1, 3, 2, 4, 3]) == 3
    assert Solution().minimumOperations(nums=[1, 2, 2, 2, 2]) == 2


if __name__ == '__main__':
    test()
