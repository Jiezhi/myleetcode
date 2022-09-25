#!/usr/bin/env python3
"""
CREATED AT: 2022-09-25

URL: https://leetcode.com/problems/sort-the-people/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 2418-SortThePeople

Difficulty: Easy

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        """
        n == names.length == heights.length
        1 <= n <= 10^3
        1 <= names[i].length <= 20
        1 <= heights[i] <= 105
        names[i] consists of lower and upper case English letters.
        All the values of heights are distinct.
        """
        p = list(zip(names, heights))
        p.sort(key=lambda x: -x[1])
        return [x[0] for x in p]


def test():
    assert Solution().sortPeople(names=["Mary", "John", "Emma"], heights=[180, 165, 170]) == ["Mary", "Emma", "John"]


if __name__ == '__main__':
    test()
