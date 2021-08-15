#!/usr/bin/env python
"""
CREATED AT: 2021/8/15
Des:
https://leetcode.com/contest/weekly-contest-254/problems/array-with-elements-not-equal-to-average-of-neighbors/
GITHUB: https://github.com/Jiezhi/myleetcode

"""
from typing import List

from tool import print_results


class Solution:
    @print_results
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        """
        暴力遍历，没有数学依据，不知道有没有漏洞
        :param nums:
        :return:
        """
        for i in range(1, len(nums) - 1):
            index = 2
            while nums[i] * 2 == nums[i - 1] + nums[i + 1]:
                if i + index < len(nums):
                    if index < 0:
                        # means go back from 0
                        # make sure before nums are in rule
                        if nums[i + 1] != nums[i + index] \
                                and nums[i + index + 1] * 2 != nums[i + index] + nums[i + index + 2]:
                            nums[i + 1], nums[i + index] = nums[i + index], nums[i + 1]
                        else:
                            index += 1
                    elif nums[i + 1] != nums[i + index]:
                        nums[i + 1], nums[i + index] = nums[i + index], nums[i + 1]
                    else:
                        index += 1
                else:
                    # index to the end of nums,
                    # just go back
                    index = -i
        return nums


def test():
    nums = [1, 2, 3, 4, 5]
    ret = Solution().rearrangeArray(nums)
    assert sum(nums) == sum(ret) and len(nums) == len(ret)
    for r in ret:
        assert r in nums
    for i in range(1, len(ret) - 2):
        assert ret[i] * 2 != ret[i - 1] + ret[i + 1]


if __name__ == '__main__':
    test()
