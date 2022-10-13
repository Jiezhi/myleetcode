#!/usr/bin/env python3
"""
CREATED AT: 2022-10-13

URL: https://leetcode.com/problems/max-chunks-to-make-sorted/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 769-MaxChunksToMakeSorted

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        """
        Runtime: 60 ms, faster than 27.13%
        Memory Usage: 13.8 MB, less than 96.57%

        n == arr.length
        1 <= n <= 10
        0 <= arr[i] < n
        All the elements of arr are unique.
        """
        ret = 0
        cur_max, i = arr[0], 0
        while i < len(arr):
            cur_max = max(cur_max, arr[i])
            if i >= cur_max:
                ret += 1
            i += 1
        return ret


def test():
    assert Solution().maxChunksToSorted(arr=[4, 3, 2, 1, 0]) == 1
    assert Solution().maxChunksToSorted(arr=[1, 0, 2, 3, 4]) == 4
    assert Solution().maxChunksToSorted(arr=[0, 1, 2, 3, 4]) == 5


if __name__ == '__main__':
    test()
