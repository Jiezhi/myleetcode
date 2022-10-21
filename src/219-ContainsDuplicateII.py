#!/usr/bin/env python3
"""
CREATED AT: 2022-08-08

URL: https://leetcode.com/problems/contains-duplicate-ii/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 219-ContainsDuplicateII

Difficulty: Easy

Desc: 

Tag: 

See:  217, 220

"""
from tool import *


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        2022-10-21
        Runtime: 760 ms, faster than 81.02%
        Memory Usage: 27.6 MB, less than 14.95%

        1 <= nums.length <= 10^5
        -10^9 <= nums[i] <= 10^9
        0 <= k <= 10^5
        """
        pos = {}
        for i, num in enumerate(nums):
            if num in pos and i - pos[num] <= k:
                return True
            pos[num] = i
        return False

    def containsNearbyDuplicate2(self, nums: List[int], k: int) -> bool:
        """
        51 / 51 test cases passed.
        Status: Accepted
        Runtime: 1186 ms, faster than 18.87%
        Memory Usage: 27.4 MB, less than 24.47%

        1 <= nums.length <= 10^5
        -10^9 <= nums[i] <= 10^9
        0 <= k <= 10^5
        """
        cnt = collections.Counter(nums[:k + 1])
        if any(True for x in cnt.keys() if cnt[x] > 1):
            return True

        for i, num in enumerate(nums[k + 1:], k + 1):
            cnt[nums[i - k - 1]] -= 1
            if cnt[num] > 0:
                return True
            cnt[num] = 1
        return False


def test():
    assert Solution().containsNearbyDuplicate(nums=[1, 2, 3, 1], k=3)
    assert Solution().containsNearbyDuplicate(nums=[1, 0, 1, 1], k=1)
    assert not Solution().containsNearbyDuplicate(nums=[1, 2, 3, 1, 2, 3], k=2)


if __name__ == '__main__':
    test()
