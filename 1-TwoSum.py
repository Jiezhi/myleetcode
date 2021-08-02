"""
 https://leetcode.com/problems/two-sum
 https://leetcode.com/explore/challenge/card/august-leetcoding-challenge-2021/613/week-1-august-1st-august-7th/3836/
 @Author: Jiezhi
 @Date: 2018-07-06 17:35:15 
 @Last Modified by:   Jiezhi
 @Last Modified time:  20210802
 """
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        54 / 54 test cases passed.
        Status: Accepted
        Runtime: 632 ms
        Memory Usage: 14.6 MB
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            result = target - nums[i]
            if result in nums[i + 1:]:
                return [i, i + 1 + nums[i + 1:].index(result)]


def test():
    assert Solution().twoSum([2, 7, 11, 15], 9) == [0, 1]


if __name__ == '__main__':
    test()
