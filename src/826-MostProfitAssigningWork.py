#!/usr/bin/env python3
"""
CREATED AT: 2022-06-16

URL: https://leetcode.com/problems/most-profit-assigning-work/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 826-MostProfitAssigningWork

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
import bisect
from typing import List


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        """
        Runtime: 638 ms, faster than 30.63%
        Memory Usage: 17.1 MB, less than 68.92%

        n == difficulty.length
        n == profit.length
        m == worker.length
        1 <= n, m <= 10^4
        1 <= difficulty[i], profit[i], worker[i] <= 10^5
        """
        sorted_zip = sorted(zip(difficulty, profit))
        d, p = [0], [0]
        cur_max = 0
        for i, j in sorted_zip:
            d.append(i)
            cur_max = max(cur_max, j)
            p.append(cur_max)
        return sum(p[bisect.bisect(d, x) - 1] for x in worker)


def test():
    assert Solution().maxProfitAssignment(
        difficulty=[2, 4, 6, 8, 10], profit=[10, 20, 30, 40, 50],
        worker=[4, 5, 6, 7]) == 100
    assert Solution().maxProfitAssignment(
        difficulty=[85, 47, 57],
        profit=[24, 66, 99], worker=[40, 25, 25]) == 0
    assert Solution().maxProfitAssignment(
        [68, 35, 52, 47, 86],
        [67, 17, 1, 81, 3],
        [92, 10, 85, 84, 82]) == 324


if __name__ == '__main__':
    test()
