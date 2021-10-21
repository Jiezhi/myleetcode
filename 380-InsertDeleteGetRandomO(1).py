#!/usr/bin/env python
"""
CREATED AT: 2021/10/21
Des:
https://leetcode.com/problems/insert-delete-getrandom-o1/
https://leetcode.com/explore/interview/card/top-interview-questions-medium/112/design/813/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tags: Design

Reference: https://leetcode.com/problems/insert-delete-getrandom-o1/discuss/85397/Simple-solution-in-Python/221668
"""
import random


class RandomizedSet:
    """
    19 / 19 test cases passed.
    Status: Accepted
    Runtime: 529 ms
    Memory Usage: 61.7 MB
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums, self.pos = [], {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.pos:
            return False
        self.nums.append(val)
        self.pos[val] = len(self.nums) - 1
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.pos:
            return False
        index = self.pos[val]
        last_value = self.nums[-1]

        self.nums[index] = last_value
        self.pos[last_value] = index

        self.nums.pop()
        del self.pos[val]
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.nums)


def test():
    obj = RandomizedSet()
    obj.insert(5)
    assert obj.getRandom() == 5
    assert not obj.insert(5)
    assert not obj.remove(4)
    assert obj.remove(5)


if __name__ == '__main__':
    test()
