#!/usr/bin/env python
"""
Github: https://github.com/Jiezhi/myleetcode

Created on 2019-07-29

Leetcode: https://leetcode.com/problems/pascals-triangle-ii/

"""


class Solution:
    def getNextRow(self, row: list):
        newRow = [1]
        for i in range(len(row) - 1):
            newRow.append(row[i] + row[i + 1])
        newRow.append(1)
        return newRow

    def getRow(self, rowIndex: int) -> list:
        lastRow = [1]
        for i in range(rowIndex):
            lastRow = self.getNextRow(lastRow)
        return lastRow


def test():
    assert Solution().getRow(0) == [1]
    assert Solution().getRow(1) == [1, 1]
    assert Solution().getRow(3) == [1, 3, 3, 1]


if __name__ == '__main__':
    test()
