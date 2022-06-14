#!/usr/bin/env python3
"""
CREATED AT: 2022-06-14

URL: https://leetcode.com/problems/frequency-of-the-most-frequent-element/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1838-FrequencyOfTheMostFrequentElement

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        """
        Ref: https://leetcode.com/problems/frequency-of-the-most-frequent-element/discuss/1175090/JavaC%2B%2BPython-Sliding-Window
        Runtime: 2421 ms, faster than 28.03% 
        Memory Usage: 28.6 MB, less than 10.59% 
        1 <= nums.length <= 10^5
        1 <= nums[i] <= 10^5
        1 <= k <= 10^5
        """
        ret = 1
        nums = sorted(nums)
        i, j, n = 0, 1, len(nums)
        acc = 0
        while j < n:
            while acc <= k and j < n:
                ret = max(ret, j - i)
                acc += (nums[j] - nums[j - 1]) * (j - i)
                j += 1
            if acc <= k:
                ret = max(ret, j - i)
            while acc > k and i <= j:
                acc -= (nums[j - 1] - nums[i])
                i += 1
        return ret


def test():
    assert Solution().maxFrequency(nums=[1000], k=1000) == 1
    assert Solution().maxFrequency(nums=[1, 2, 4], k=5) == 3
    assert Solution().maxFrequency(nums=[1, 4, 8, 13], k=5) == 2
    assert Solution().maxFrequency(nums=[3, 9, 6], k=2) == 1


if __name__ == '__main__':
    test()
