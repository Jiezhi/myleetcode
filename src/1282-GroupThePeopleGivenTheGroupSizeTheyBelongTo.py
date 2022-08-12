#!/usr/bin/env python3
"""
CREATED AT: 2022-08-12

URL: https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1282-GroupThePeopleGivenTheGroupSizeTheyBelongTo

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        """
        Runtime: 95 ms, faster than 78.84%
        Memory Usage: 14 MB, less than 88.49%

        groupSizes.length == n
        1 <= n <= 500
        1 <= groupSizes[i] <= n
        """
        ret = []
        tmp = collections.defaultdict(list)
        for i, size in enumerate(groupSizes):
            if size == 1:
                ret.append([i])
                continue
            tmp[size].append(i)
            if len(tmp[size]) == size:
                ret.append(tmp[size])
                tmp[size] = []
        return ret


def test():
    assert Solution().groupThePeople(groupSizes=[3, 3, 3, 3, 3, 1, 3]) == [[0, 1, 2], [5], [3, 4, 6]]
    assert Solution().groupThePeople(groupSizes=[2, 1, 3, 3, 3, 2]) == [[1], [2, 3, 4], [0, 5]]


if __name__ == '__main__':
    test()
