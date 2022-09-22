#!/usr/bin/env python3
"""
CREATED AT: 2022-09-22

URL: https://leetcode.com/problems/two-sum/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1-TwoSum

Difficulty: Easy

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        2022-09-22
        Runtime: 183 ms, faster than 35.85%
        Memory Usage: 16.8 MB, less than 8.86%
        2 <= nums.length <= 10^4
        -10^9 <= nums[i] <= 10^9
        -10^9 <= target <= 10^9
        Only one valid answer exists.
        """
        pos_dict = defaultdict(list)
        for pos, num in enumerate(nums):
            pos_dict[num].append(pos)
        if target & 1 == 0 and len(pos_dict[target // 2]) >= 2:
            return pos_dict[target // 2][:2]
        for num in set(nums):
            v = target - num
            if v != num and v in pos_dict:
                return [pos_dict[num][0], pos_dict[v][0]]

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        """
        2018-07-06 17:35:15
        20210802
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
    assert Solution().twoSum2([2, 7, 11, 15], 9) == [0, 1]


if __name__ == '__main__':
    test()
