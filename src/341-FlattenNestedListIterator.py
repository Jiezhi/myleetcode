#!/usr/bin/env python
"""
CREATED AT: 2022/5/8
Des:
https://leetcode.com/problems/flatten-nested-list-iterator/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
import collections


class NestedInteger:
    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """
        pass

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """
        pass

    def getList(self) -> ['NestedInteger']:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """
        pass


class NestedIterator:
    """
    Runtime: 133 ms, faster than 8.82%
    Memory Usage: 17.9 MB, less than 41.16%
    1 <= nestedList.length <= 500
    The values of the integers in the nested list is in the range [-10^6, 10^6].
    """

    def __init__(self, nestedList: [NestedInteger]):
        self.dq = collections.deque(nestedList)

    def next(self) -> int:
        return self.dq.popleft()

    def hasNext(self) -> bool:
        while self.dq:
            if self.dq[0].isInteger():
                return True
            else:
                node = self.dq.popleft()
                self.dq.extendleft(node.getList()[::-1])
        return False


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

def test():
    # No test here for now
    pass


if __name__ == '__main__':
    test()
