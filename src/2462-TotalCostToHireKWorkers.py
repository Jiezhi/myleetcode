#!/usr/bin/env python3
"""
CREATED AT: 2022-11-06

URL: https://leetcode.com/problems/total-cost-to-hire-k-workers/
https://leetcode.com/contest/weekly-contest-318/problems/total-cost-to-hire-k-workers/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 2462-TotalCostToHireKWorkers

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        """
        1 <= costs.length <= 10^5
        1 <= costs[i] <= 10^5
        1 <= k, candidates <= costs.length
        """
        n = len(costs)
        if k == len(costs):
            return sum(costs)
        ret = 0
        hq = []
        l, r = 0, n - 1
        for i in range(candidates):
            if r - i < i:
                break
            heapq.heappush(hq, (costs[i], i, 'L'))
            if r - i > i:
                heapq.heappush(hq, (costs[r - i], r - i, 'R'))
            else:
                break
        l, r = candidates, r - candidates
        hq2 = []
        while k > 0:
            k -= 1
            if not hq2:
                tmp = heapq.heappop(hq)
                cost = tmp[0]
                heapq.heappush(hq2, (tmp[1], tmp[0], tmp[2]))
                while hq and hq[0][0] == cost:
                    tmp = heapq.heappop(hq)
                    heapq.heappush(hq2, (tmp[1], tmp[0], tmp[2]))
            if hq and hq[0][0] < hq2[0][1]:
                tmp = heapq.heappop(hq)
                d = tmp[2]
                ret += tmp[0]
            else:
                tmp = heapq.heappop(hq2)
                d = tmp[2]
                ret += tmp[1]
            if 0 <= l <= r < len(costs):
                if d == 'L':
                    if hq2 and costs[l] == hq2[0][1]:
                        heapq.heappush(hq2, (l, costs[l], 'L'))
                    else:
                        heapq.heappush(hq, (costs[l], l, 'L'))
                    l += 1
                else:
                    if hq2 and costs[r] == hq2[0][1]:
                        heapq.heappush(hq2, (r, costs[r], 'R'))
                    else:
                        heapq.heappush(hq, (costs[r], r, 'R'))
                    r -= 1
        return ret


def test():
    assert Solution().totalCost(costs=[17, 12, 10, 2, 7, 2, 11, 20, 8], k=3, candidates=4) == 11
    assert Solution().totalCost(costs=[1, 2, 4, 1], k=3, candidates=3) == 4


if __name__ == '__main__':
    test()
