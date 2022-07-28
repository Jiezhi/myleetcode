#!/usr/bin/env python3
"""
CREATED AT: 2022-07-28

URL: https://leetcode.com/problems/rank-transform-of-an-array/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1331-RankTransformOfAnArray

Difficulty: Easy

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        """
        Runtime: 655 ms, faster than 24.45%
        Memory Usage: 33.4 MB, less than 47.92%
        0 <= arr.length <= 10^5
        -10^9 <= arr[i] <= 10^9
        """
        dct = {k: i for i, k in enumerate(sorted(set(arr)), 1)}
        return [dct[v] for v in arr]


def test():
    assert Solution().arrayRankTransform(arr=[40, 10, 20, 30]) == [4, 1, 2, 3]
    assert Solution().arrayRankTransform(arr=[100, 100, 100]) == [1, 1, 1]


if __name__ == '__main__':
    test()
