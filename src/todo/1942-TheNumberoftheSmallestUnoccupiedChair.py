#!/usr/bin/env python
"""
CREATED AT: 2021/7/24
Des:
https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair
https://leetcode.com/contest/biweekly-contest-57/problems/the-number-of-the-smallest-unoccupied-chair/
GITHUB: https://github.com/Jiezhi/myleetcode

"""
from typing import List


class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        t_arrival = times[targetFriend][0]
        sorted_times = sorted(times, key=lambda x: x[0])
        char_stack = []
        # for t in sorted_times:

        # print(t_arrival)
        t_char = 0
        for t in sorted_times:
            if t[0] == t_arrival:
                return t_char
            # print(t)
            if t[0] < t_arrival:
                t_char += 1
            if t[1] <= t_arrival:
                t_char -= 1
            print(f'{t} - {t_char}')
        # print(t_char)
        return t_char


def test():
    # assert Solution().smallestChair([[1, 4], [2, 3], [4, 6]], 1) == 1
    # assert Solution().smallestChair([[3, 10], [1, 5], [2, 6]], 0) == 2

    assert Solution().smallestChair(
        [[33889, 98676], [80071, 89737], [44118, 52565],
         [52992, 84310], [78492, 88209], [21695, 67063],
         [84622, 95452], [98048, 98856], [98411, 99433],
         [55333, 56548], [65375, 88566], [55011, 62821],
         [48548, 48656], [87396, 94825], [55273, 81868],
         [75629, 91467]], 6) == 2


if __name__ == '__main__':
    test()
