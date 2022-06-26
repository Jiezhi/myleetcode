#!/usr/bin/env python3
"""
CREATED AT: 2022-06-26

URL: https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1423-MaximumPointsYouCanObtainFromCards

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        """
        Runtime: 544 ms, faster than 59.98%
        Memory Usage: 27.4 MB, less than 40.17%

        1 <= cardPoints.length <= 10^5
        1 <= cardPoints[i] <= 10^4
        1 <= k <= cardPoints.length
        """
        if k == len(cardPoints):
            return sum(cardPoints)

        s = sum(cardPoints[:k])
        ret = s
        for i in range(k - 1, -1, -1):
            s = s - cardPoints[i] + cardPoints[i - k]
            ret = max(ret, s)
        return ret


def test():
    assert Solution().maxScore([1, 2, 3, 4, 5, 6, 1], 3) == 12
    assert Solution().maxScore(cardPoints=[9, 7, 7, 9, 7, 7, 9], k=7) == 55


if __name__ == '__main__':
    test()
