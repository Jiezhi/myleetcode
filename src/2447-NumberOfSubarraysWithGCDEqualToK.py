#!/usr/bin/env python3
"""
CREATED AT: 2022-10-23

URL: https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/
https://leetcode.com/contest/weekly-contest-316/problems/number-of-subarrays-with-gcd-equal-to-k/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 2447-NumberOfSubarraysWithGCDEqualToK

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        """
        1 <= nums.length <= 1000
        1 <= nums[i], k <= 10^9
        """
        nums = [x // k if x % k == 0 else -1 for x in nums]
        ret = 0

        for i, num in enumerate(nums):
            if num == 1:
                ret += 1
            elif num == -1:
                continue
            j = i + 1
            gcd = num
            while j < len(nums) and nums[j] != -1:
                if gcd != 1:
                    gcd = math.gcd(gcd, nums[j])
                if gcd == 1:
                    ret += 1
                j += 1
        return ret


def test():
    assert Solution().subarrayGCD(nums=[9, 3, 1, 2, 6, 3], k=3) == 4
    assert Solution().subarrayGCD(nums=[4], k=7) == 0


if __name__ == '__main__':
    test()
