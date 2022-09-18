#!/usr/bin/env python3
"""
CREATED AT: 2022-09-18

URL: https://leetcode.com/problems/maximum-matching-of-players-with-trainers/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 2410-MaximumMatchingOfPlayersWithTrainers

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        """
        1 <= players.length, trainers.length <= 10^5
        1 <= players[i], trainers[j] <= 10^9
        """
        ret = 0
        players.sort()
        trainers.sort()
        i, j = 0, 0
        while i < len(players) and j < len(trainers):
            if players[i] <= trainers[j]:
                ret += 1
                i += 1
                j += 1
            else:
                j += 1
        return ret


def test():
    assert Solution().matchPlayersAndTrainers(players=[4, 7, 9], trainers=[8, 2, 5, 8]) == 2
    assert Solution().matchPlayersAndTrainers(players=[1, 1, 1], trainers=[10]) == 1


if __name__ == '__main__':
    test()
