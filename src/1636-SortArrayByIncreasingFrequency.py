#!/usr/bin/env python3
"""
CREATED AT: 2022-09-19

URL: https://leetcode.com/problems/sort-array-by-increasing-frequency/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1636-SortArrayByIncreasingFrequency

Difficulty: Easy

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        """
        Runtime: 101 ms, faster than 30.55%
        Memory Usage: 13.9 MB, less than 22.19%
        1 <= nums.length <= 100
        -100 <= nums[i] <= 100
        """
        nums = sorted(Counter(nums).items(), key=lambda x: [x[1], -x[0]])
        ret = []
        for num, cnt in nums:
            ret.extend([num] * cnt)
        return ret

    def frequencySort2(self, nums: List[int]) -> List[int]:
        """
        https://leetcode.cn/problems/sort-array-by-increasing-frequency/solution/an-zhao-pin-lu-jiang-shu-zu-sheng-xu-pai-z2db/
        :param nums:
        :return:
        """
        cnt = Counter(nums)
        nums.sort(key=lambda x: (cnt[x], -x))
        return nums


def test():
    assert Solution().frequencySort(nums=[1, 1, 2, 2, 2, 3]) == [3, 1, 1, 2, 2, 2]
    assert Solution().frequencySort(nums=[2, 3, 1, 3, 2]) == [1, 3, 3, 2, 2]
    assert Solution().frequencySort(nums=[-1, 1, -6, 4, 5, -6, 1, 4, 1]) == [5, -1, 4, 4, -6, -6, 1, 1, 1]


if __name__ == '__main__':
    test()
