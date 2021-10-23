#!/usr/bin/env python
"""
CREATED AT: 2021/9/13
Des:
https://leetcode.com/problems/longest-increasing-subsequence/
https://leetcode.com/explore/interview/card/top-interview-questions-medium/111/dynamic-programming/810/
https://leetcode.com/study-plan/dynamic-programming
GITHUB: https://github.com/Jiezhi/myleetcode

Reference: https://leetcode.com/problems/longest-increasing-subsequence/discuss/74824/JavaPython-Binary-search-O(nlogn)-time-with-explanation
https://en.wikipedia.org/wiki/Patience_sorting
Difficulty: Medium
"""
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        1 <= nums.length <= 2500
        -104 <= nums[i] <= 104
        :param nums:
        :return:
        """
        pass


def test():
    assert Solution().lengthOfLIS(nums=[10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert Solution().lengthOfLIS(nums=[0, 1, 0, 3, 2, 3]) == 4
    assert Solution().lengthOfLIS(nums=[7, 7, 7, 7, 7, 7, 7]) == 1


if __name__ == '__main__':
    test()
