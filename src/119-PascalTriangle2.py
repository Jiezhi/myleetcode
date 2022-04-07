#!/usr/bin/env python
"""
Github: https://github.com/Jiezhi/myleetcode

Created on 2019-07-29

Leetcode: https://leetcode.com/problems/pascals-triangle-ii/

"""
from typing import List


class Solution:
    def getRow2(self, rowIndex: int) -> List[int]:
        """
        34 / 34 test cases passed.
        Status: Accepted
        Runtime: 47 ms, faster than 42.34%
        Memory Usage: 13.9 MB, less than 0
        :param rowIndex: 0 <= rowIndex <= 33
        :return:
        """
        if rowIndex == 0:
            return [1]
        ret = [1] * rowIndex
        for i in range(2, rowIndex + 1):
            pre = ret[0]
            for j in range(1, i):
                ret[j], pre = pre + ret[j], ret[j]
        return ret + [1]

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
    assert Solution().getRow2(3) == [1, 3, 3, 1]


if __name__ == '__main__':
    test()
