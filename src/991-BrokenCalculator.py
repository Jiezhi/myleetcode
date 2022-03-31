#!/usr/bin/env python
"""
CREATED AT: 2022/3/23
Des:

https://leetcode.com/problems/broken-calculator/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""


class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        """
        Runtime: 50 ms, faster than 33.79%
        Memory Usage: 13.8 MB, less than 73.06%

        1 <= x, y <= 10^9
        """
        if startValue >= target:
            return startValue - target

        cnt = 0
        while target > startValue:
            target, left = divmod(target, 2)
            if left:
                target += 1
            cnt += 1 + left

        return cnt + startValue - target


def test():
    assert Solution().brokenCalc(startValue=2, target=3) == 2
    assert Solution().brokenCalc(startValue=5, target=8) == 2
    assert Solution().brokenCalc(startValue=3, target=10) == 3


if __name__ == '__main__':
    test()
