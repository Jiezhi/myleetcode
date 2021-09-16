#!/usr/bin/env python
"""
Github: https://github.com/Jiezhi/myleetcode

Created on 2019-08-16
Updated on 2021-09-16

Leetcode: https://leetcode.com/problems/spiral-matrix/
https://leetcode.com/explore/item/3977

"""

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        23 / 23 test cases passed.
        Status: Accepted
        Runtime: 41 ms
        Memory Usage: 14.3 MB
        :param matrix:
        :return:
        """
        if not matrix:
            return []
        # get horizontal and vertical length
        len_h = len(matrix[0])
        len_v = len(matrix)

        # set border
        min_v, min_h, max_v, max_h = 0, -1, len_v, len_h
        # min_v, min_h, max_v, max_h = 0, 0, len_v - 1, len_h - 1
        i, j = 0, 0

        # set direction
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        curr_d = 0
        ret = []
        while (min_h < j < max_h) or (min_v < i < max_v):
            # Add
            ret.append(matrix[i][j])
            # Bound check
            d_flag = curr_d % 4
            if directions[d_flag] == (0, 1) and j + 1 == max_h:
                max_h -= 1
                curr_d += 1
                d_flag = curr_d % 4
            elif directions[d_flag] == (1, 0) and i + 1 == max_v:
                max_v -= 1
                curr_d += 1
                d_flag = curr_d % 4
            elif directions[d_flag] == (0, -1) and j - 1 == min_h:
                min_h += 1
                curr_d += 1
                d_flag = curr_d % 4
            elif directions[d_flag] == (-1, 0) and i - 1 == min_v:
                min_v += 1
                curr_d += 1
                d_flag = curr_d % 4
            # Move forward
            i, j = i + directions[d_flag][0], j + directions[d_flag][1]
        return ret


def test():
    assert Solution().spiralOrder([[1, 2], [3, 4]]) == [1, 2, 4, 3]
    assert Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]


if __name__ == '__main__':
    test()
