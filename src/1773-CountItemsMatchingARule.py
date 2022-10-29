#!/usr/bin/env python3
"""
CREATED AT: 2022-10-29

URL: https://leetcode.com/problems/count-items-matching-a-rule/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1773-CountItemsMatchingARule

Difficulty: Easy

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        """
        Runtime: 261 ms, faster than 88.21%
        Memory Usage: 20.2 MB, less than 86.36%
        1 <= items.length <= 10^4
        1 <= typei.length, colori.length, namei.length, ruleValue.length <= 10
        ruleKey is equal to either "type", "color", or "name".
        All strings consist only of lowercase letters.
        """
        if ruleKey == 'type':
            i = 0
        elif ruleKey == 'color':
            i = 1
        else:
            i = 2
        return sum(1 for x in items if x[i] == ruleValue)


def test():
    assert Solution().countMatches(
        items=[["phone", "blue", "pixel"], ["computer", "silver", "lenovo"], ["phone", "gold", "iphone"]],
        ruleKey="color", ruleValue="silver") == 1
    assert Solution().countMatches(
        items=[["phone", "blue", "pixel"], ["computer", "silver", "phone"], ["phone", "gold", "iphone"]],
        ruleKey="type", ruleValue="phone") == 2


if __name__ == '__main__':
    test()
