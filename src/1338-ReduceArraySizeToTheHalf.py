#!/usr/bin/env python3
"""
CREATED AT: 2022-08-18

URL: https://leetcode.com/problems/reduce-array-size-to-the-half/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1338-ReduceArraySizeToTheHalf

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        """
        Runtime: 718 ms, faster than 81.19%
        Memory Usage: 31.8 MB, less than 81.83%

        2 <= arr.length <= 10^5
        arr.length is even.
        1 <= arr[i] <= 10^5
        """
        cnt = collections.Counter(arr)
        cnt = [-x for x in cnt.values()]
        heapq.heapify(cnt)
        ret, total = 0, 0
        while total < (len(arr) + 1) // 2:
            ret += 1
            total -= heapq.heappop(cnt)
        return ret


def test():
    assert Solution().minSetSize(arr=[3, 3, 3, 3, 5, 5, 5, 2, 2, 7]) == 2
    assert Solution().minSetSize(arr=[7, 7, 7, 7, 7, 7]) == 1


if __name__ == '__main__':
    test()
