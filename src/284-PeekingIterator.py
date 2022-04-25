#!/usr/bin/env python
"""
CREATED AT: 2022/4/25
Des:
https://leetcode.com/problems/peeking-iterator/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""


# Below is the interface for Iterator, which is already defined for you.
#
class Iterator:
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """
        self.nums = nums
        self.index = 0

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """
        return self.index < len(self.nums)

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """
        self.index += 1
        return self.nums[self.index - 1]


class PeekingIterator:
    """
    Runtime: 38 ms, faster than 72.25%
    Memory Usage: 14.2 MB, less than 29.71%

    1 <= nums.length <= 1000
    1 <= nums[i] <= 1000
    All the calls to next and peek are valid.
    At most 1000 calls will be made to next, hasNext, and peek.
    """

    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.cur = None
        self.iter = iterator

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if not self.cur:
            self.cur = self.iter.next()
        return self.cur

    def next(self):
        """
        :rtype: int
        """
        if self.cur:
            val = self.cur
            self.cur = None
            return val
        else:
            return self.iter.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.cur is not None or self.iter.hasNext()


def test():
    iter = PeekingIterator(Iterator([1, 2, 3, 4]))
    assert iter.hasNext()
    assert iter.peek() == 1
    assert iter.next() == 1
    assert iter.next() == 2
    assert iter.next() == 3
    assert iter.next() == 4
    assert not iter.hasNext()


if __name__ == '__main__':
    test()
