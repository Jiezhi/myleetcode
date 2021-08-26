#!/usr/bin/env python
"""
https://leetcode.com/problems/container-with-most-water/
Created on 2018-12-13

@author: 'Jiezhi.G@gmail.com'

Reference: 
"""


class Solution:
    def maxArea(self, height):
        """
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
    assert Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert Solution().maxArea([1, 2]) == 1


if __name__ == '__main__':
    test()
