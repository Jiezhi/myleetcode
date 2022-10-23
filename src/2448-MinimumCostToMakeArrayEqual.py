#!/usr/bin/env python3
"""
CREATED AT: 2022-10-23

URL: https://leetcode.com/problems/minimum-cost-to-make-array-equal/
https://leetcode.com/contest/weekly-contest-316/problems/minimum-cost-to-make-array-equal/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 2448-MinimumCostToMakeArrayEqual

Difficulty: Hard

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        """
        n == nums.length == cost.length
        1 <= n <= 10^5
        1 <= nums[i], cost[i] <= 10^6
        """

        def cost_take(x):
            return sum(abs(x - num) * cost[i] for i, num in enumerate(nums))

        seen = set()

        def find_min_cost(lo, hi):
            if (lo, hi) in seen:
                ret = math.inf
                for num in range(min(nums), max(nums) + 1):
                    r = cost_take(num)
                    ret = min(r, ret)
                return ret
            lo_cost, hi_cost = cost_take(lo), cost_take(hi)
            seen.add((lo, hi))
            if lo <= hi:
                mid = (hi + lo) // 2
                mid_cost = cost_take(mid)
                if lo_cost <= mid <= hi_cost:
                    return lo_cost
                elif lo_cost >= mid >= hi_cost:
                    return hi_cost
                else:
                    another_cost = cost_take(mid + 1)
                    if another_cost <= mid_cost:
                        return min(find_min_cost(mid + 1, hi), another_cost)
                    else:
                        return min(find_min_cost(lo, mid - 1), mid_cost)
            else:
                return math.inf

        return find_min_cost(min(nums), max(nums))


def test():
    assert Solution().minCost(nums=[1, 3, 5, 2], cost=[2, 3, 1, 14]) == 8
    assert Solution().minCost(nums=[2, 2, 2, 2, 2], cost=[4, 2, 8, 1, 3]) == 0


if __name__ == '__main__':
    test()
