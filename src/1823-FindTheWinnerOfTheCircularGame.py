#!/usr/bin/env python
"""
CREATED AT: 2022/4/6
Des:
https://leetcode.com/problems/find-the-winner-of-the-circular-game/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: 

Tag: 

See: 

"""


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        """
        Runtime: 567 ms, faster than 12.11%
        Memory Usage: 13.8 MB, less than 80.94%

        :param n: 1 <= k <= n <= 500
        :param k:
        :return:
        """
        if k == 1:
            return n
        arr = [i for i in range(1, n + 1)]
        pre = 0
        while len(arr) > 1:
            new_arr = []
            for i, v in enumerate(arr):
                if (i + 1 + pre) % k == 0:
                    continue
                else:
                    new_arr.append(v)
            pre = (len(arr) + pre) % k
            arr = new_arr
        return arr[0]


def test():
    assert Solution().findTheWinner(n=5, k=2) == 3
    assert Solution().findTheWinner(n=6, k=5) == 1


if __name__ == '__main__':
    test()
