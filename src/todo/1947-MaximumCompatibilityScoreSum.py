#!/usr/bin/env python
"""
CREATED AT: 2021/7/25
Des:
https://leetcode.com/problems/maximum-compatibility-score-sum
https://leetcode.com/contest/weekly-contest-251/problems/maximum-compatibility-score-sum/
GITHUB: https://github.com/Jiezhi/myleetcode

"""
from typing import List


class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        pairs = []
        max_score = 0
        total_score = 0
        n = len(students[0])
        p_cnt = len(students)
        for s in students:
            pair = []
            for m in mentors:
                score = 0
                for i in range(n):
                    if s[i] == m[i]:
                        score += 1
                pair.append(score)
                max_score = max(max_score, score)
            pairs.append(pair)
        print(pairs)
        while True:
            max_score = 0
            pos_i = -1
            pos_j = -1
            for i in range(p_cnt):
                for j in range(p_cnt):
                    if pairs[i][j] > max_score:
                        max_score = pairs[i][j]
                        pos_i = i
                        pos_j = j
            if max_score == 0:
                return total_score
            total_score += max_score
            for i in range(p_cnt):
                pairs[i][pos_j] = 0
            for j in range(p_cnt):
                pairs[pos_i][j] = 0


def test():
    assert Solution().maxCompatibilitySum(
        [[1, 1, 1], [0, 0, 1], [0, 0, 1], [0, 1, 0]],
        [[1, 0, 1], [0, 1, 1], [0, 1, 0], [1, 1, 0]]
    ) == 9

    assert Solution().maxCompatibilitySum(
        students=[[1, 1, 0], [1, 0, 1], [0, 0, 1]],
        mentors=[[1, 0, 0], [0, 0, 1], [1, 1, 0]]
    ) == 8

    assert Solution().maxCompatibilitySum(
        students=[[0, 0], [0, 0], [0, 0]],
        mentors=[[1, 1], [1, 1], [1, 1]]
    ) == 0


if __name__ == '__main__':
    test()
