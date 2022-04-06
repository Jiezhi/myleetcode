#!/usr/bin/env python
"""
CREATED AT: 2022/4/6
Des:
https://leetcode.com/problems/3sum-with-multiplicity/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""
import collections
import math
from typing import List


class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        """
        Runtime: 90 ms, faster than 83.72%
        Memory Usage: 14.2 MB, less than 7.56%
        :param arr: 3 <= arr.length <= 3000
                    0 <= arr[i] <= 100

        :param target: 0 <= target <= 300
        :return:
        """
        modulo = 10 ** 9 + 7
        cnt = collections.Counter(arr)
        arr = sorted(set(arr))
        ret = 0
        for i, v in enumerate(arr):
            if v * 3 == target:
                if cnt[v] > 2:
                    ret += math.comb(cnt[v], 3)
                    ret %= modulo
            elif cnt[v] > 1:
                ret += cnt[target - v * 2] * math.comb(cnt[v], 2)
                ret %= modulo

            leftover = target - v
            lo, hi = i + 1, len(arr) - 1
            while lo < hi:
                if arr[lo] + arr[hi] == leftover:
                    ret += cnt[v] * cnt[arr[lo]] * cnt[arr[hi]]
                    ret %= modulo
                    lo += 1
                    hi -= 1
                elif arr[lo] + arr[hi] < leftover:
                    lo += 1
                else:
                    hi -= 1
        return ret


def test():
    assert Solution().threeSumMulti(arr=[1, 1, 2, 2, 3, 3, 4, 4, 5, 5], target=8) == 20
    assert Solution().threeSumMulti(arr=[1, 1, 2, 2, 2, 2], target=5) == 12


if __name__ == '__main__':
    test()
