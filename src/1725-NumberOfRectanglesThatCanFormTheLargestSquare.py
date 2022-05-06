#!/usr/bin/env python
"""
CREATED AT: 2022/5/6
Des:
https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

"""
from typing import List


class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        """
        Runtime: 207 ms, faster than 72.28%
        Memory Usage: 14.6 MB, less than 27.44%
        1 <= rectangles.length <= 1000
        rectangles[i].length == 2
        1 <= li, wi <= 10^9
        li != wi
        :param rectangles:
        :return:
        """
        maxl, cnt = 0, 0
        for l, w in rectangles:
            tmpl = min(l, w)
            if tmpl > maxl:
                maxl = tmpl
                cnt = 1
            elif tmpl == maxl:
                cnt += 1
        return cnt


def test():
    assert Solution().countGoodRectangles(rectangles=[[5, 8], [3, 9], [5, 12], [16, 5]]) == 3


if __name__ == '__main__':
    test()
