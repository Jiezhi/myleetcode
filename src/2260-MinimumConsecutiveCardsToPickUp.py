#!/usr/bin/env python
"""
CREATED AT: 2022/5/1
Des:
https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""
from typing import List


class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        """
        1 <= cards.length <= 10^5
        0 <= cards[i] <= 10^6
        """
        ret = len(cards) + 2
        cnt = {}
        for i, value in enumerate(cards):
            if value in cnt:
                ret = min(ret, i - cnt[value] + 1)
                if ret == 2:
                    return 2
            cnt[value] = i
        return ret if ret < len(cards) + 2 else -1


def test():
    assert Solution().minimumCardPickup(cards=[3, 4, 2, 3, 4, 7]) == 4
    assert Solution().minimumCardPickup(cards=[1, 0, 5, 3]) == -1


if __name__ == '__main__':
    test()
