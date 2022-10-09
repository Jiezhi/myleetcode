#!/usr/bin/env python3
"""
CREATED AT: 2022-10-09

URL: https://leetcode.com/contest/weekly-contest-314/problems/the-employee-that-worked-on-the-longest-task/
https://leetcode.com/problems/the-employee-that-worked-on-the-longest-task/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 2432-TheEmployeeThatWorkedOnTheLongestTask

Difficulty: Easy

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        """
        2 <= n <= 500
        1 <= logs.length <= 500
        logs[i].length == 2
        0 <= idi <= n - 1
        1 <= leaveTimei <= 500
        idi != idi+1
        leaveTimei are sorted in a strictly increasing order.
        """
        ret = logs[0]
        for i, log in enumerate(logs[1:], 1):
            diff = log[1] - logs[i - 1][1]
            if diff > ret[1]:
                ret = [log[0], diff]
            elif diff == ret[1]:
                ret = [min(log[0], ret[0]), diff]
        return ret[0]


def test():
    assert Solution().hardestWorker(n=10, logs=[[0, 3], [2, 5], [0, 9], [1, 15]]) == 1
    assert Solution().hardestWorker(n=26, logs=[[1, 1], [3, 7], [2, 12], [7, 17]]) == 3
    assert Solution().hardestWorker(n=2, logs=[[0, 10], [1, 20]]) == 0


if __name__ == '__main__':
    test()
