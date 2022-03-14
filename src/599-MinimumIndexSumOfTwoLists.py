#!/usr/bin/env python
"""
CREATED AT: 2022/3/14
Des:
https://leetcode.com/problems/minimum-index-sum-of-two-lists/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

"""
from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        """
        Runtime: 156 ms, faster than 88.50%
        Memory Usage: 14.4 MB, less than 58.31%

        1 <= list1.length, list2.length <= 1000
        1 <= list1[i].length, list2[i].length <= 30
        list1[i] and list2[i] consist of spaces ' ' and English letters.
        All the stings of list1 are unique.
        All the stings of list2 are unique.
        """
        l1_dict = dict()
        for i in range(len(list1)):
            l1_dict[list1[i]] = i
        ret = []
        min_ret = 2000
        for i in range(len(list2)):
            if list2[i] not in l1_dict:
                continue
            s = i + l1_dict[list2[i]]
            if s == min_ret:
                ret.append(list2[i])
            elif s < min_ret:
                min_ret = s
                ret.clear()
                ret.append(list2[i])
        return ret


def test():
    assert Solution().findRestaurant(
        list1=["Shogun", "Tapioca Express", "Burger King", "KFC"],
        list2=["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
    ) == ["Shogun"]


if __name__ == '__main__':
    test()
