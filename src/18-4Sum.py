#!/usr/bin/env python
"""
CREATED AT: 2021/9/16
Des:
https://leetcode.com/problems/4sum/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium
"""
from typing import List

from tool import print_results


class Solution:
    @print_results
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        286 / 286 test cases passed.
        Status: Accepted
        Runtime: 1063 ms
        Memory Usage: 14.5 MB
        :param nums:
        :param target:
        :return:
        """
        if len(nums) < 4:
            return []
        nums = sorted(nums)
        l = 0
        ret = []
        last_l = None

        while l < len(nums) - 2:
            if nums[l] == last_l:
                l += 1
                continue
            last_l = nums[l]
            last_h = None
            h = len(nums) - 1
            while h > l + 2:
                if nums[h] == last_h:
                    h -= 1
                    continue
                last_i = None
                last_h = nums[h]
                for i in range(l + 1, h - 1):
                    if nums[i] == last_i:
                        continue
                    last_i = nums[i]
                    leftover = target - nums[l] - nums[h] - nums[i]
                    if not nums[i] <= leftover <= nums[h]:
                        if nums[i] > leftover:
                            break
                        else:
                            continue
                    if leftover in nums[i + 1:h]:
                        ret.append([nums[l], nums[i], leftover, nums[h]])
                h -= 1
            l += 1
        return ret


def test():
    assert Solution().fourSum(nums=[2, 2, 2, 2, 2], target=8) == [[2, 2, 2, 2]]
    ans = [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
    ret = Solution().fourSum(nums=[1, 0, -1, 0, -2, 2], target=0)
    assert len(ret) == len(ans)
    for a in ans:
        assert a in ret


if __name__ == '__main__':
    test()
