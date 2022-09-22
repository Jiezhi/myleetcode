#!/usr/bin/env python3
"""
CREATED AT: 2022-09-22

URL: https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1545-FindKthBitInNthBinaryString

Difficulty: Medium

Desc: 

Tag: 

See: 

"""


class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        """
        Runtime: 50 ms, faster than 81.75%
        Memory Usage: 14 MB, less than 64.55%

        1 <= n <= 20
        1 <= k <= 2^n - 1
        """
        lens = [1] * n
        for i in range(1, n):
            lens[i] = lens[i - 1] * 2 + 1

        n -= 1
        k -= 1

        def dfs(n, k) -> int:
            if n == 0:
                return 0
            if k == 0:
                return 0
            mid = lens[n] // 2
            if k == mid:
                return 1
            if k < mid:
                return dfs(n - 1, k)
            else:
                return dfs(n - 1, lens[n] - k - 1) ^ 1

        return str(dfs(n, k))


def test():
    assert Solution().findKthBit(n=3, k=1) == '0'
    assert Solution().findKthBit(n=4, k=11) == '1'


if __name__ == '__main__':
    test()
