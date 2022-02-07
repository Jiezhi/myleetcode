#!/usr/bin/env python
"""
CREATED AT: 2022/2/7
Des:

https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
https://leetcode.com/explore/featured/card/heap/646/practices/4086/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

Time Spent:  min
"""
import heapq
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """
        CREATED AT: 2022/2/7
        Ref: https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/85173/Share-my-thoughts-and-Clean-Java-Code
        86 / 86 test cases passed.
        Status: Accepted
        Runtime: 216 ms, faster than 65.04%
        Memory Usage: 18.8 MB, less than 63.88%

        n == matrix.length == matrix[i].length
        1 <= n <= 300
        -10^9 <= matrix[i][j] <= 10^9
        All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
        1 <= k <= n^2
        :param matrix:
        :param k:
        :return:
        """
        n = len(matrix)
        heap = [(matrix[0][x], (0, x)) for x in range(n)]
        heapq.heapify(heap)
        for i in range(k - 1):
            _, (x, y) = heapq.heappop(heap)
            if x == n - 1:
                continue
            heapq.heappush(heap, (matrix[x + 1][y], (x + 1, y)))
        return heapq.heappop(heap)[0]


def test():
    assert Solution().kthSmallest(matrix=[[1, 5, 9], [10, 11, 13], [12, 13, 15]], k=8) == 13
    assert Solution().kthSmallest(matrix=[[-5]], k=1) == -5


if __name__ == '__main__':
    test()
