#!/usr/bin/env python3
"""
CREATED AT: 2022-08-09

URL: https://leetcode.com/problems/binary-trees-with-factors/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 823-BinaryTreesWithFactors

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        """
        Runtime: 1286 ms, faster than 13.63%
        Memory Usage: 14.1 MB, less than 57.07%

        1 <= arr.length <= 1000
        2 <= arr[i] <= 10^9
        All the values of arr are unique.
        """
        MOD = 10 ** 9 + 7
        arr.sort()
        cnt = collections.Counter(arr)
        for i in range(len(arr)):
            for j in range(i):
                a, b = divmod(arr[i], arr[j])
                if b == 0 and a in cnt:
                    cnt[arr[i]] += cnt[arr[j]] * cnt[a] % MOD
        return sum(cnt.values()) % MOD


def test():
    assert Solution().numFactoredBinaryTrees(arr=[2, 3, 4, 6, 8, 12]) == 23
    assert Solution().numFactoredBinaryTrees(arr=[2, 4]) == 3
    assert Solution().numFactoredBinaryTrees(arr=[2, 4, 5, 10]) == 7


if __name__ == '__main__':
    test()
