#!/usr/bin/env python3
"""
CREATED AT: 2022-10-06

URL: https://leetcode.com/problems/three-equal-parts/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 927-ThreeEqualParts

Difficulty: Hard

Desc: 

Tag: 

See: A better way: https://leetcode.cn/problems/three-equal-parts/solution/san-deng-fen-by-leetcode-solution-3l2y/

"""
from tool import *


class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        """
        Runtime: 3258 ms, faster than 5.19%
        Memory Usage: 15.1 MB, less than 67.53%

        3 <= arr.length <= 3 * 10^4
        arr[i] is 0 or 1
        """
        n = len(arr)
        arr = arr[::-1]
        last_one = -1
        j = n - 1
        while j >= 0:
            if arr[j] == 1:
                last_one = j
                break
            j -= 1
        if last_one == -1:
            return [0, 2]
        first_one = arr.index(1)
        if first_one == last_one:
            return [-1, -1]

        cur = arr[:first_one + 1]
        for i in range(first_one + 1, n - 1):
            if len(cur) + i > last_one:
                return [-1, -1]

            if cur == arr[i:len(cur) + i]:
                for j in range(len(cur) + i, n):
                    if cur == arr[j:len(cur) + j] and j <= last_one < len(cur) + j:
                        return [n - j - 1, n - i]
                    if arr[j] == 1:
                        break

            if arr[i] == 1:
                cur = arr[:i + 1]
        return [-1, -1]


def test():
    assert Solution().threeEqualParts(arr=[0, 1, 0, 0, 0, 0, 1]) == [-1, -1]
    assert Solution().threeEqualParts(arr=[1, 0, 1, 0, 1]) == [0, 3]
    assert Solution().threeEqualParts(arr=[1, 1, 0, 1, 1]) == [-1, -1]
    assert Solution().threeEqualParts(arr=[1, 1, 0, 0, 1]) == [0, 2]
    assert Solution().threeEqualParts(arr=[1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1]) == [1, 6]


if __name__ == '__main__':
    test()
