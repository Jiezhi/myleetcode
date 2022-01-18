#!/usr/bin/env python
"""
CREATED AT: 2022/1/18
Des:

https://leetcode.com/problems/can-place-flowers/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

Time Spent:  min
"""
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """
        Runtime: 284 ms, faster than 12.11%
        Memory Usage: 14.3 MB, less than 99.36%

        1 <= flowerbed.length <= 2 * 10^4
        flowerbed[i] is 0 or 1.
        There are no two adjacent flowers in flowerbed.
        0 <= n <= flowerbed.length
        :param flowerbed:
        :param n:
        :return:
        """
        if n == 0:
            return True
        ret = 0
        i = 0
        while i < len(flowerbed) and ret < n:
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (
                    i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                ret += 1
            if ret >= n:
                return True
            i += 1

        return False


def test():
    assert Solution().canPlaceFlowers(flowerbed=[0], n=1)
    assert Solution().canPlaceFlowers(flowerbed=[1, 0, 0, 0, 0, 0, 1], n=2)
    assert Solution().canPlaceFlowers(flowerbed=[0, 0, 1, 0, 1], n=1)
    assert Solution().canPlaceFlowers(flowerbed=[0, 0, 1, 0, 0], n=2)
    assert Solution().canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1], n=1)
    assert not Solution().canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1], n=2)
    assert not Solution().canPlaceFlowers(flowerbed=[1, 0, 1, 0, 1, 0, 1], n=1)
    assert not Solution().canPlaceFlowers(flowerbed=[1, 0, 0, 0, 0, 1], n=2)


if __name__ == '__main__':
    test()
