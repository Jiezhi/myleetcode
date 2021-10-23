#!/usr/bin/env python
"""
Github: https://github.com/Jiezhi/myleetcode

Created on 2019-07-29

Leetcode: https://leetcode.com/problems/pascals-triangle/

"""


class Solution:
    def getNextRow(self, row: list):
        newRow = [1]
        for i in range(len(row) - 1):
            newRow.append(row[i] + row[i + 1])
        newRow.append(1)
        return newRow

    def generate(self, numRows: int):
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        ret = [[1]]
        lastRow = [1]
        for i in range(1, numRows):
            lastRow = self.getNextRow(lastRow)
            ret.append(lastRow)
        return ret


def test():
    assert Solution().generate(5) == [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1]
    ]


if __name__ == '__main__':
    test()
