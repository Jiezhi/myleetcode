#!/usr/bin/env python
"""
CREATED AT: 2022/2/17
Des:

https://leetcode.com/problems/combination-sum/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 322 Coin Change

Time Spent: 10 min
"""
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        CREATED AT: 2022/2/17
        Runtime: 69 ms, faster than 87.96%
        Memory Usage: 14.5 MB, less than 8.65%
        1 <= candidates.length <= 30
        1 <= candidates[i] <= 200
        All elements of candidates are distinct.
        1 <= target <= 500
        """
        ret = [[] for _ in range(target)]
        for candidate in candidates:
            if candidate <= target:
                ret[candidate - 1].append([candidate])
            for i in range(target):
                if i + candidate < target:
                    for combination in ret[i]:
                        tmp_combination = combination.copy()
                        tmp_combination.append(candidate)
                        ret[i + candidate].append(tmp_combination)
        return ret[-1]


def test():
    assert Solution().combinationSum(candidates=[2], target=1) == []


if __name__ == '__main__':
    test()
