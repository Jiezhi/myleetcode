#!/usr/bin/env python
"""
CREATED AT: 2022/2/8
Des:

GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: Graph

See: 

Time Spent:  min
"""
import collections
import sys
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
        CREATED AT: 2022/2/8
        50 / 50 test cases passed.
        Status: Accepted
        Runtime: 278 ms, faster than 35.32%
        Memory Usage: 15.2 MB, less than 68.36%
        1 <= n <= 100
        0 <= flights.length <= (n * (n - 1) / 2)
        flights[i].length == 3
        0 <= from_i, to_i < n
        from_i != to_i
        1 <= price_i <= 10^4
        There will not be any multiple flights between two cities.
        0 <= src, dst, k < n
        src != dst
        :param n:
        :param flights:
        :param src:
        :param dst:
        :param k:
        :return:
        """
        pre_dp = [sys.maxsize] * n
        cur_dp = [sys.maxsize] * n
        pre_dp[src] = 0
        # vertex output edge relations
        flight_dict = collections.defaultdict(list)
        for flight in flights:
            flight_dict[flight[0]].append((flight[1], flight[2]))
        cur_level = set()
        cur_level.add(src)
        for _ in range(k + 1):
            next_level = set()
            for vertex in cur_level:
                for flight in flight_dict[vertex]:
                    cur_dp[flight[0]] = min(cur_dp[flight[0]], pre_dp[vertex] + flight[1])
                    next_level.add(flight[0])
            cur_level = next_level.copy()
            pre_dp = cur_dp.copy()

        return cur_dp[dst] if cur_dp[dst] != sys.maxsize else -1


def test():
    assert Solution().findCheapestPrice(n=4, flights=[[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1]], src=0, dst=3,
                                        k=1) == 6
    assert Solution().findCheapestPrice(n=3, flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]], src=0, dst=2, k=0) == 500
    assert Solution().findCheapestPrice(n=3, flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]], src=0, dst=2, k=1) == 200


if __name__ == '__main__':
    test()
