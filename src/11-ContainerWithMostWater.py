#!/usr/bin/env python
"""

https://leetcode.com/problems/container-with-most-water/
https://leetcode.com/explore/interview/card/top-interview-questions-hard/116/array-and-strings/830/

Created on 2018-12-13
Updated at 2022/01/04

@author: 'Jiezhi.G@gmail.com'

Reference: https://leetcode.com/problems/container-with-most-water/solution/

Difficulty: Medium
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Updated at 2022/01/04
        Runtime: 1491 ms, faster than 5.01%
        Memory Usage: 27.6 MB, less than 22.34%

        n == height.length
        2 <= n <= 10^5
        0 <= height[i] <= 10^4
        :param height:
        :return:
        """
        low, high = 0, len(height) - 1
        ret = 0
        while low < high:
            ret = max(min(height[low], height[high]) * (high - low), ret)
            if height[low] <= height[high]:
                low += 1
            else:
                high -= 1
        return ret

    def maxArea2(self, height):
        """
        Updated at 2018-12-13
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        max_value = 0
        top = max(height)
        while i < j:
            if top * (j - i) < max_value:
                break
            max_value = max(max_value, min(height[i], height[j]) * (j - i))
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return max_value


def test():
    assert Solution().maxArea(height=list(range(1000))) == 249500
    assert Solution().maxArea(height=[1, 2, 3, 4, 5, 4, 3, 2, 1]) == 12
    assert Solution().maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert Solution().maxArea(height=[1, 2]) == 1


if __name__ == '__main__':
    test()
