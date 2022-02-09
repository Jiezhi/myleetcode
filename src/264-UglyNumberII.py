#!/usr/bin/env python
"""
CREATED AT: 2021/10/8
Des:
https://leetcode.com/problems/ugly-number-ii/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium
"""
import heapq


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        """
        CREATED AT: 2022/2/9
        Runtime: 169 ms, faster than 70.85%
        Memory Usage: 13.9 MB, less than 97.90%
        Ref: https://leetcode.com/problems/ugly-number-ii/discuss/69364/My-16ms-C%2B%2B-DP-solution-with-short-explanation
        Runtime: 192 ms, faster than 61.82%
        Memory Usage: 14.2 MB, less than 76.37%
        :param n: 1 <= n <= 1690
        :return:
        """
        if n == 1:
            return 1
        p1, p2, p3 = 0, 0, 0
        dp = [1]
        i = 1
        while i < n:
            dp.append(min(2 * dp[p1], 3 * dp[p2], 5 * dp[p3]))
            if dp[-1] == 2 * dp[p1]:
                p1 += 1
            if dp[-1] == 3 * dp[p2]:
                p2 += 1
            if dp[-1] == 5 * dp[p3]:
                p3 += 1
            i += 1
        return dp[-1]

    def nthUglyNumber2(self, n: int) -> int:
        """
        CREATED AT: 2022/2/9
        Runtime: 192 ms, faster than 61.82%
        Memory Usage: 14.2 MB, less than 76.37%
        :param n: 1 <= n <= 1690
        :return:
        """
        if n == 1:
            return 1
        heap = [1]
        i = 1
        visited = set()
        factors = [2, 3, 5]
        while i < n:
            last = heapq.heappop(heap)
            for factor in factors:
                if last * factor not in visited:
                    visited.add(last * factor)
                    heapq.heappush(heap, last * factor)
            i += 1
        return heap[0]


def test():
    assert Solution().nthUglyNumber(n=9) == 10
    assert Solution().nthUglyNumber(n=10) == 12
    assert Solution().nthUglyNumber(n=1) == 1


if __name__ == '__main__':
    test()
