#!/usr/bin/env python3
"""
CREATED AT: 2022-09-22

URL: https://leetcode.com/problems/check-array-formation-through-concatenation/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1640-CheckArrayFormationThroughConcatenation

Difficulty: Easy

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        """
        Runtime: 79 ms, faster than 37.14%
        Memory Usage: 13.9 MB, less than 29.98%
        1 <= pieces.length <= arr.length <= 100
        sum(pieces[i].length) == arr.length
        1 <= pieces[i].length <= arr.length
        1 <= arr[i], pieces[i][j] <= 100
        The integers in arr are distinct.
        The integers in pieces are distinct (i.e., If we flatten pieces in a 1D array, all the integers in this array are distinct).
        """
        pos = {}
        for i, p in enumerate(pieces):
            pos[p[0]] = i

        i = 0
        while i < len(arr):
            if arr[i] not in pos:
                return False
            for num in pieces[pos[arr[i]]]:
                if num != arr[i]:
                    return False
                i += 1
        return True


def test():
    assert Solution().canFormArray(arr=[15, 88], pieces=[[88], [15]])
    assert not Solution().canFormArray(arr=[49, 18, 16], pieces=[[16, 18, 49]])
    assert Solution().canFormArray(arr=[91, 4, 64, 78], pieces=[[78], [4, 64], [91]])


if __name__ == '__main__':
    test()
