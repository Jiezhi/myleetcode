#!/usr/bin/env python
"""
CREATED AT: 2022/3/25
Des:
https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

"""
from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        """
        Runtime: 24 ms, faster than 99.26%
        Memory Usage: 13.9 MB, less than 12.89%

        :param salary: 3 <= salary.length <= 100
                       1000 <= salary[i] <= 10^6
                       All the integers of salary are unique.
        :return:
        """
        min_s, max_s = 10 ** 6 + 1, 0
        total = 0
        for s in salary:
            min_s = min(min_s, s)
            max_s = max(max_s, s)
            total += s
        return (total - min_s - max_s) / (len(salary) - 2)


def test():
    assert Solution().average([4000, 3000, 1000, 2000]) == 2500.0


if __name__ == '__main__':
    test()
