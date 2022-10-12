#!/usr/bin/env python
"""
CREATED AT: 2021/8/28
Des:
https://leetcode.com/problems/increasing-triplet-subsequence/
https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/781/
GITHUB: https://github.com/Jiezhi/myleetcode

"""
from tool import *


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        """
        2021/8/28
        76 / 76 test cases passed.
        Status: Accepted
        Runtime: 695 ms
        Memory Usage: 25.5 MB
        :param nums:
        :return:
        """
        n = len(nums)
        if n < 3:
            return False
        # set by Constraints1,
        # flag_num means that there is nums[i] < nums[j] and flag_num is the smallest nums[j]
        flag_num = 2 ** 31
        min_value = nums[0]
        for i in range(1, n):
            if nums[i] > flag_num:
                return True
            if nums[i] > min_value:
                flag_num = min(nums[i], flag_num)
            min_value = min(min_value, nums[i])
        return False

    def increasingTriplet2(self, nums: List[int]) -> bool:
        """
        20221011
        Runtime: 897 ms, faster than 64.93%
        Memory Usage: 24.6 MB, less than 80.42%
        1 <= nums.length <= 5 * 10^5
        -2^31 <= nums[i] <= 2^31 - 1
        """
        if len(nums) < 3:
            return False
        pre, middle = nums[0], math.inf
        for num in nums[1:]:
            if num > middle:
                return True
            if pre < num < middle:
                middle = num
            elif num < pre:
                pre = num
        return False


def test():
    assert Solution().increasingTriplet(nums=[1, 2, 3, 4, 5])
    assert not Solution().increasingTriplet(nums=[5, 4, 3, 2, 1])
    assert Solution().increasingTriplet(nums=[2, 1, 5, 0, 4, 6])
    assert Solution().increasingTriplet(nums=[2, 1, 5, 0, 6])


if __name__ == '__main__':
    test()
