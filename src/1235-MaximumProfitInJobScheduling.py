#!/usr/bin/env python3
"""
CREATED AT: 2022-10-22

URL: https://leetcode.com/problems/maximum-profit-in-job-scheduling/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1235-MaximumProfitInJobScheduling

Difficulty: Hard

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        """
        https://leetcode.cn/problems/maximum-profit-in-job-scheduling/solution/gui-hua-jian-zhi-gong-zuo-by-leetcode-so-gu0e/
        Runtime: 1436 ms, faster than 39.93%
        Memory Usage: 26.4 MB, less than 78.04%
        """
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        dp = [0] * (len(jobs) + 1)
        for i in range(1, len(jobs) + 1):
            pos = bisect.bisect(jobs, jobs[i - 1][0], hi=i, key=lambda x: x[1])
            dp[i] = max(dp[pos] + jobs[i - 1][2], dp[i - 1])

        return dp[-1]

    def jobScheduling2(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        """
        TLE
        1 <= startTime.length == endTime.length == profit.length <= 5 * 10^4
        1 <= startTime[i] < endTime[i] <= 10^9
        1 <= profit[i] <= 10^4
        """
        jobs = []
        for s, e, p in sorted(zip(startTime, endTime, profit), key=lambda x: [x[0], x[1], [2]]):
            while jobs:
                job = jobs[-1]
                if e <= job[1] and p >= job[2] and s >= job[0]:
                    jobs.pop()
                else:
                    break
            jobs.append((s, e, p))
        starts = [x[0] for x in jobs]

        @cache
        def dp(i: int, j: int) -> int:
            if i > jobs[-1][0] or j >= len(starts):
                return 0
            pos = bisect.bisect_left(starts, i, j)
            return max(jobs[pos][2] + dp(jobs[pos][1], j + 1), dp(i, j + 1))

        return dp(0, 0)


def test():
    assert Solution().jobScheduling(startTime=[1, 2, 3, 3], endTime=[3, 4, 5, 6], profit=[50, 10, 40, 70]) == 120
    assert Solution().jobScheduling(startTime=[1, 2, 3, 4, 6], endTime=[3, 5, 10, 6, 9],
                                    profit=[20, 20, 100, 70, 60]) == 150
    assert Solution().jobScheduling(startTime=[1, 1, 1], endTime=[2, 3, 4], profit=[5, 6, 4]) == 6


if __name__ == '__main__':
    test()
