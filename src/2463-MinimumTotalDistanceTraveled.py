#!/usr/bin/env python3
"""
CREATED AT: 2022-11-07

URL: https://leetcode.com/problems/minimum-total-distance-traveled/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 2463-MinimumTotalDistanceTraveled

Difficulty: Hard

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        """
        Ref: https://leetcode.cn/problems/minimum-total-distance-traveled/discuss/2783305/Python-DP-Solution
        Runtime: 2908 ms, faster than 50.00%
        Memory Usage: 445.2 MB, less than 100.00%
        1 <= robot.length, factory.length <= 100
        factory[j].length == 2
        -10^9 <= robot[i], positionj <= 10^9
        0 <= limitj <= robot.length
        The input will be generated such that it is always possible to repair every robot.
        """

        robot.sort()
        factory.sort()

        @cache
        def dp(i, j, k) -> int:
            if i == len(robot):
                return 0
            if j == len(factory):
                return math.inf
            return min(dp(i, j + 1, 0),
                       dp(i + 1, j, k + 1) + abs(robot[i] - factory[j][0]) if factory[j][1] > k else math.inf)

        return dp(0, 0, 0)

    def minimumTotalDistance2(self, robot: List[int], factory: List[List[int]]) -> int:
        """
        1 <= robot.length, factory.length <= 100
        factory[j].length == 2
        -10^9 <= robot[i], positionj <= 10^9
        0 <= limitj <= robot.length
        The input will be generated such that it is always possible to repair every robot.
        """
        cnt = Counter()
        for p, l in factory:
            if l > 0:
                cnt[p] = l
        rob = []
        for r in robot:
            if cnt[r] > 0:
                cnt[r] -= 1
            else:
                rob.append(r)

        dq = collections.deque([(rob, cnt, 0)])
        ret = math.inf
        while dq:
            rob, cnt, step = dq.popleft()
            if not rob:
                ret = min(ret, step)
                continue
            rob_copy = rob.copy()
            r = rob_copy.pop()
            for fp in cnt.keys():
                cnt_copy = cnt.copy()
                if cnt_copy[fp] == 1:
                    del cnt_copy[fp]
                else:
                    cnt_copy[fp] -= 1
                dq.append((rob_copy, cnt_copy, step + abs(fp - r)))
        return ret


def test():
    assert Solution().minimumTotalDistance(
        [670355988, 403625544, 886437985, 224430896, 126139936, -477101480, -868159607, -293937930],
        [[333473422, 7], [912209329, 7], [468372740, 7], [-765827269, 4], [155827122, 4], [635462096, 2],
         [-300275936, 2], [-115627659, 0]]) == 509199280
    assert Solution().minimumTotalDistance(robot=[0, 4, 6], factory=[[2, 2], [6, 2]]) == 4
    assert Solution().minimumTotalDistance(robot=[1, -1], factory=[[-2, 1], [2, 1]]) == 2


if __name__ == '__main__':
    test()
