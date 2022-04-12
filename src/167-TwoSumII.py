#!/usr/bin/env python
"""
Github: https://github.com/Jiezhi/myleetcode

Created on 2019/8/28

Leetcode: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

"""
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            if (target - numbers[i]) in numbers:
                return [i + 1, numbers.index(target - numbers[i], i + 1) + 1]

    def twoSum2(self, numbers: List[int], target: int) -> List[int]:
        """
        Runtime: 340 ms, faster than 5.04%
        Memory Usage: 14.9 MB, less than 91.23%

        2 <= numbers.length <= 3 * 10^4
        -1000 <= numbers[i] <= 1000
        numbers is sorted in non-decreasing order.
        -1000 <= target <= 1000
        The tests are generated such that there is exactly one solution.

        :param numbers:
        :param target:
        :return:
        """
        n = len(numbers)
        for i, num in enumerate(numbers):
            lo, hi = i + 1, n - 1
            while lo <= hi:
                mid = lo + (hi - lo) // 2
                if numbers[mid] + num == target:
                    return [i + 1, mid + 1]
                elif numbers[mid] + num < target:
                    lo = mid + 1
                else:
                    hi = mid - 1

    def twoSum3(self, numbers: List[int], target: int) -> List[int]:
        """
        Runtime: 203 ms, faster than 35.81%
        Memory Usage: 15.1 MB, less than 12.87%

        :param numbers:
        :param target:
        :return:
        """
        lo, hi = 0, len(numbers) - 1
        while lo < hi:
            if numbers[lo] + numbers[hi] == target:
                return [lo + 1, hi + 1]
            elif numbers[lo] + numbers[hi] < target:
                lo += 1
            else:
                hi -= 1


def test():
    assert Solution().twoSum([2, 7, 11, 15], 9) == [1, 2]
    assert Solution().twoSum([0, 0, 3, 4], 0) == [1, 2]


if __name__ == '__main__':
    test()
