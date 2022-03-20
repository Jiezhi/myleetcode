#!/usr/bin/env python
"""
CREATED AT: 2022/3/20
Des:

GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""
from typing import List


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        """
        Runtime: 1160 ms, faster than 88.96%
        Memory Usage: 15.2 MB, less than 44.98%

        2 <= tops.length <= 2 * 104
        bottoms.length == tops.length
        1 <= tops[i], bottoms[i] <= 6
        """
        n = len(tops)

        top_head = tops[0]
        bottom_head = bottoms[0]

        top1_head, ret1 = True, 0
        bottom1_head, ret2 = True, 0

        top2_head, ret3 = True, 1
        bottom2_head, ret4 = True, 1

        for i in range(1, n):
            if not top1_head and not bottom1_head and not top2_head and not bottom2_head:
                return -1
            if top1_head:
                if tops[i] == top_head:
                    pass
                elif bottoms[i] == top_head:
                    ret1 += 1
                else:
                    top1_head = False
                    ret1 = n
            if bottom1_head:
                if bottoms[i] == bottom_head:
                    pass
                elif tops[i] == bottom_head:
                    ret2 += 1
                else:
                    bottom1_head = False
                    ret2 = n
            if top2_head:
                if bottoms[i] == top_head:
                    pass
                elif tops[i] == top_head:
                    ret3 += 1
                else:
                    top2_head = False
                    ret3 = n
            if bottom2_head:
                if tops[i] == bottom_head:
                    pass
                elif bottoms[i] == bottom_head:
                    ret4 += 1
                else:
                    bottom2_head = False
                    ret4 = n
        return min(ret1, ret2, ret3, ret4)


def test():
    assert Solution().minDominoRotations([2, 1, 2, 4, 2, 2], [5, 2, 6, 2, 3, 2]) == 2
    assert Solution().minDominoRotations([3, 5, 1, 2, 3], [3, 6, 3, 3, 4]) == -1


if __name__ == '__main__':
    test()
