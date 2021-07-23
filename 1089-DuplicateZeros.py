#!/usr/bin/env python
"""
CREATED AT: 2021/7/23
Des:

https://leetcode.com/problems/duplicate-zeros/
https://leetcode.com/explore/featured/card/fun-with-arrays/525/inserting-items-into-an-array/3245/

GITHUB: https://github.com/Jiezhi/myleetcode

"""
from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.

        Just create a new array, and set the value to the old arr.
        """
        arr_len = len(arr)
        new_arr = []
        for num in arr:
            new_arr.append(num)
            if num == 0:
                new_arr.append(0)
            if len(new_arr) == arr_len:
                break
        for i in range(arr_len):
            arr[i] = new_arr[i]

    def duplicateZeros2(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.

        In place the arr from the end when encounter zero.
        """
        arr_len = len(arr)
        i = 0
        # The last one number don't need handle
        while i < arr_len - 1:
            if arr[i] == 0:
                for j in range(arr_len - 1, i, -1):
                    arr[j] = arr[j - 1]
                # jump over the duplicate zero
                i += 2
            else:
                # move forward
                i += 1


def test():
    arr = [1, 0, 2, 3, 0, 4, 5, 0]
    Solution().duplicateZeros(arr)
    assert arr == [1, 0, 0, 2, 3, 0, 0, 4]

    arr = [1, 2, 3]
    Solution().duplicateZeros(arr)
    assert arr == [1, 2, 3]

    arr = [1, 0, 2, 3, 0, 4, 5, 0]
    Solution().duplicateZeros2(arr)
    assert arr == [1, 0, 0, 2, 3, 0, 0, 4]

    arr = [1, 2, 3]
    Solution().duplicateZeros2(arr)
    assert arr == [1, 2, 3]


if __name__ == '__main__':
    test()
