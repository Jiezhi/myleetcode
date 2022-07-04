#!/usr/bin/env python3
"""
CREATED AT: 2022-07-04

URL: https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1465-MaximumAreaOfAPieceOfCakeAfterHorizontalAndVerticalCuts

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from typing import List


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        """
        Runtime: 584 ms, faster than 19.34% 
        Memory Usage: 27.3 MB, less than 43.27% 

        2 <= h, w <= 10^9
        1 <= horizontalCuts.length <= min(h - 1, 10^5)
        1 <= verticalCuts.length <= min(w - 1, 10^5)
        1 <= horizontalCuts[i] < h
        1 <= verticalCuts[i] < w
        All the elements in horizontalCuts are distinct.
        All the elements in verticalCuts are distinct.
        """
        hs = [0] + sorted(horizontalCuts) + [h]
        vs = [0] + sorted(verticalCuts) + [w]

        def getMaxDiff(nums) -> int:
            ret = 0
            for i in range(1, len(nums)):
                ret = max(ret, nums[i] - nums[i - 1])
            return ret

        return getMaxDiff(hs) * getMaxDiff(vs) % (10 ** 9 + 7)


def test():
    assert Solution().maxArea(h=5, w=4, horizontalCuts=[1, 2, 4], verticalCuts=[1, 3]) == 4
    assert Solution().maxArea(h=5, w=4, horizontalCuts=[3, 1], verticalCuts=[1]) == 6
    assert Solution().maxArea(h=5, w=4, horizontalCuts=[3], verticalCuts=[3]) == 9


if __name__ == '__main__':
    test()
