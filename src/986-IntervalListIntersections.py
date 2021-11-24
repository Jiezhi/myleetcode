#!/usr/bin/env python
"""
CREATED AT: 2021/11/24
Des:

https://leetcode.com/problems/interval-list-intersections/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 
"""
from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        """
        Runtime: 232 ms, faster than 14.13%
        Memory Usage: 15.4 MB, less than 9.89%

        0 <= firstList.length, secondList.length <= 1000
        firstList.length + secondList.length >= 1
        0 <= starti < endi <= 10^9
        endi < starti+1
        0 <= startj < endj <= 10^9
        endj < startj+1
        :param firstList:
        :param secondList:
        :return:
        """
        ret = []
        i, j = 0, 0
        while i < len(firstList) and j < len(secondList):
            first = firstList[i]
            second = secondList[j]
            if first[0] > second[1]:
                j += 1
            elif second[0] > first[1]:
                i += 1
            else:
                if first[0] <= second[0] <= first[1]:
                    if first[1] == second[1]:
                        ret.append([second[0], first[1]])
                        i += 1
                        j += 1
                    elif first[1] < second[1]:
                        ret.append([second[0], first[1]])
                        i += 1
                    else:
                        ret.append([second[0], second[1]])
                        j += 1

                elif second[0] <= first[0] <= second[1]:
                    if first[1] == second[1]:
                        ret.append([first[0], first[1]])
                        i += 1
                        j += 1
                    elif first[1] < second[1]:
                        ret.append([first[0], first[1]])
                        i += 1
                    else:
                        ret.append([first[0], second[1]])
                        j += 1
        return ret


def test():
    assert Solution().intervalIntersection(
        firstList=[[0, 2], [5, 10], [13, 23], [24, 25]],
        secondList=[[1, 5], [8, 12], [15, 24], [25, 26]]
    ) == [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]

    assert Solution().intervalIntersection(firstList=[[1, 3], [5, 9]], secondList=[]) == []
    assert Solution().intervalIntersection(firstList=[[1, 7]], secondList=[[3, 10]]) == [[3, 7]]


if __name__ == '__main__':
    test()
