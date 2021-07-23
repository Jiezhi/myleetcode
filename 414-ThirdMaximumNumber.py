#!/usr/bin/env python
"""
CREATED AT: 2021/7/23
Des:
https://leetcode.com/problems/third-maximum-number/
https://leetcode.com/explore/featured/card/fun-with-arrays/523/conclusion/3231/
GITHUB: https://github.com/Jiezhi/myleetcode

"""
from math import inf
from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        m1 = nums[0]
        m2 = None
        m3 = None
        for n in nums[1:]:
            if n == m1 or n == m2 or n == m3:
                continue
            if m1 <= n:
                m3 = m2
                m2 = m1
                m1 = n
            elif not m2:
                m2 = n
            elif m2 <= n:
                m3 = m2
                m2 = n
            elif not m3:
                m3 = n
            elif m3 < n:
                m3 = n
        # print(f'm1: {m1}, m2: {m2}, m3:{m3}')
        return m3 if m3 is not None else m1

    def thirdMax1(self, nums: List[int]) -> int:
        m1 = nums[0]
        m2 = -inf
        m3 = -inf
        for n in nums[1:]:
            if n == m1 or n == m2 or n == m3:
                continue
            if m1 <= n:
                m3 = m2
                m2 = m1
                m1 = n
            elif m2 <= n:
                m3 = m2
                m2 = n
            elif m3 < n:
                m3 = n
        # print(f'm1: {m1}, m2: {m2}, m3:{m3}')
        return m3 if m3 != -inf else m1


def test():
    assert Solution().thirdMax([3, 2, 1]) == 1
    assert Solution().thirdMax([3, 3, 3]) == 3
    assert Solution().thirdMax([1, 2, 3]) == 1
    assert Solution().thirdMax([1, 2]) == 2
    assert Solution().thirdMax([1]) == 1
    assert Solution().thirdMax([2, 2, 3, 1]) == 1
    assert Solution().thirdMax([5, 8, 3, 2, 1, 9]) == 5
    assert Solution().thirdMax([3, 3, 4, 3, 4, 3, 0, 3, 3]) == 0


if __name__ == '__main__':
    test()
