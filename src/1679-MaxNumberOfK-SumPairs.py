#!/usr/bin/env python
"""
CREATED AT: 2022/5/4
Des:
https://leetcode.com/problems/max-number-of-k-sum-pairs/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""
import collections
from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        """
        Runtime: 787 ms, faster than 63.39%
        Memory Usage: 27.2 MB, less than 17.63%
        1 <= nums.length <= 10^5
        1 <= nums[i] <= 10^9
        1 <= k <= 10^9
        :param nums:
        :param k:
        :return:
        """
        cnt = collections.Counter(nums)
        ret = 0 if k % 2 == 1 else cnt[k // 2] // 2
        for i in sorted(cnt.keys()):
            if i * 2 >= k:
                break
            ret += min(cnt[i], cnt[k - i])
        return ret


def test():
    assert Solution().maxOperations(nums=[1, 2, 3, 4], k=5) == 2
    assert Solution().maxOperations([2, 2, 2], 4) == 1


if __name__ == '__main__':
    test()
