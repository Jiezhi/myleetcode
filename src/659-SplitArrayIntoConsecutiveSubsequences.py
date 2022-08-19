#!/usr/bin/env python3
"""
CREATED AT: 2022-08-19

URL: https://leetcode.com/problems/split-array-into-consecutive-subsequences/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 659-SplitArrayIntoConsecutiveSubsequences

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        """
        Runtime: 978 ms, faster than 29.95% 
        Memory Usage: 15.3 MB, less than 25.22% 

        1 <= nums.length <= 10^4
        -1000 <= nums[i] <= 1000
        nums is sorted in non-decreasing order.
        """
        cnt = collections.Counter(nums)

        right_border = collections.defaultdict(int)

        for num in nums:
            if cnt[num] <= 0:
                continue
            if right_border[num - 1] > 0:
                cnt[num] -= 1
                right_border[num - 1] -= 1
                right_border[num] += 1
            elif cnt[num + 1] > 0 and cnt[num + 2] > 0:
                cnt[num] -= 1
                cnt[num + 1] -= 1
                cnt[num + 2] -= 1
                right_border[num + 2] += 1
            else:
                return False
        return True


def test():
    assert Solution().isPossible(nums=[1, 2, 3, 3, 4, 5])
    assert Solution().isPossible(nums=[1, 2, 3, 3, 4, 4, 5, 5])
    assert Solution().isPossible(nums=[1, 2, 3, 4, 5, 5, 6, 7])
    assert not Solution().isPossible(nums=[1, 2, 3, 4, 4, 5])


if __name__ == '__main__':
    test()
