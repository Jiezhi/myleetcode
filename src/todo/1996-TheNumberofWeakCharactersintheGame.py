#!/usr/bin/env python
"""
CREATED AT: 2021/9/5
Des:
https://leetcode.com/problems/the-number-of-weak-characters-in-the-game
https://leetcode.com/contest/weekly-contest-257/problems/the-number-of-weak-characters-in-the-game/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium
"""
from typing import List


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        cnt = 0
        properties.sort(key=lambda prop: prop[0])
        tmp_max = properties[-1]
        tmp_list = []
        current_tmp_max = tmp_max
        for i in range(len(properties) - 2, 0, -1):
            p = properties[i]
            if p[0] == current_tmp_max[0]:
                current_tmp_max[1] = max(current_tmp_max[1], p[1])
            else:
                tmp_max = current_tmp_max
                if p[1] < tmp_max[1]:
                    cnt += 1
                elif current_tmp_max[1] < p[1]:
                    current_tmp_max = p

        return cnt


def test():
    assert Solution().numberOfWeakCharacters(properties=[[7, 9], [10, 7], [6, 9], [10, 4], [7, 5], [7, 10]]) == 2
    assert Solution().numberOfWeakCharacters(properties=[[1, 1], [2, 1], [2, 2], [1, 2]]) == 1
    assert Solution().numberOfWeakCharacters(properties=[[5, 5], [6, 3], [3, 6]]) == 0
    assert Solution().numberOfWeakCharacters(properties=[[2, 2], [3, 3]]) == 1
    assert Solution().numberOfWeakCharacters(properties=[[1, 5], [10, 4], [4, 3]]) == 1


if __name__ == '__main__':
    test()
