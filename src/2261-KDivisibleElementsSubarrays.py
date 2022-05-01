#!/usr/bin/env python
"""
CREATED AT: 2022/5/1
Des:
https://leetcode.com/problems/k-divisible-elements-subarrays/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""
from typing import List


class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        """
        1 <= nums.length <= 200
        1 <= nums[i], p <= 200
        1 <= k <= nums.length
        """
        div = [True if x % p == 0 else False for x in nums]
        ret = set()
        for i in range(len(nums)):
            j = i + 1
            tmp = f'{nums[i]}'
            ret.add(tmp)
            cnt = 1 if div[i] else 0
            while j < len(nums) and cnt <= k:
                if div[j]:
                    if cnt == k:
                        break
                    cnt += 1
                tmp = f'{tmp},{nums[j]}'
                ret.add(tmp)
                j += 1
        return len(ret)


def test():
    assert Solution().countDistinct(nums=[2, 3, 3, 2, 2], k=2, p=2) == 11
    assert Solution().countDistinct(nums=[1, 2, 3, 4], k=4, p=1) == 10


if __name__ == '__main__':
    test()
