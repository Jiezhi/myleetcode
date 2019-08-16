#!/usr/bin/env python
"""
Github: https://github.com/Jiezhi/myleetcode

Created on 2019-08-15

Leetcode: https://leetcode.com/problems/diagonal-traverse/

思路：
1.获取到矩阵长宽
2.线路先是朝右上方，简计为上（up = True）
3.初始化坐标（0，0）
3.进入循环，如果坐标在矩阵内，添加到列表
4.up 为 True 的话表示朝右上方前进，i--, j++
5.up 为 False 表示朝左下方前进， i++, j--
6.重点在于边界的判断，越界分两种情况处理
7.退出循环条件为达到最后一个元素坐标
"""
from typing import List


class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        ret = []
        len_h = len(matrix[0])
        len_v = len(matrix)
        i = 0
        j = 0
        up = True
        while i < len_v or j < len_h:
            if 0 <= i < len_v and 0 <= j < len_h:
                ret.append(matrix[i][j])
                if up:
                    i -= 1
                    j += 1
                else:
                    i += 1
                    j -= 1
            elif up:
                i += 1
                # 如果移动一位后还是在边界之外，则往左下方移动一位
                if not (0 <= i < len_v and 0 <= j < len_h):
                    i += 1
                    j -= 1
                up = False
            else:
                j += 1
                # 往右上方移动
                if not (0 <= i < len_v and 0 <= j < len_h):
                    j += 1
                    i -= 1
                up = True
        return ret


def test():
    assert Solution().findDiagonalOrder([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]) == [1, 2, 4, 7, 5, 3, 6, 8, 9]

    assert Solution().findDiagonalOrder([[]]) == []
    assert Solution().findDiagonalOrder([[1], [2]]) == [1, 2]


if __name__ == '__main__':
    test()
