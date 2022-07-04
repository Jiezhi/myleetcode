#!/usr/bin/env python3
"""
CREATED AT: 2022-07-04

URL: https://leetcode.com/problems/candy/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 135-Candy

Difficulty: Hard

Desc: 

Tag: 

See: 

"""
from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        """
        Runtime: 179 ms, faster than 87.90% 
        Memory Usage: 16.8 MB, less than 37.74% 

        n == ratings.length
        1 <= n <= 2 * 10^4
        0 <= ratings[i] <= 2 * 10^4
        """
        ret = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                ret[i] = ret[i - 1] + 1
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                ret[i] = max(ret[i], ret[i + 1] + 1)

        return sum(ret)


def test():
    assert Solution().candy(ratings=[1, 0, 2]) == 5
    assert Solution().candy(ratings=[1, 2, 2]) == 4


if __name__ == '__main__':
    test()
