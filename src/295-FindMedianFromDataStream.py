#!/usr/bin/env python
"""
CREATED AT: 2022/4/24
Des:
https://leetcode.com/problems/find-median-from-data-stream/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Hard

Tag: 

See: 

"""
import heapq


class MedianFinder:
    """
    Runtime: 657 ms, faster than 62.18%
    Memory Usage: 36 MB, less than 68.41%

    -10^5 <= num <= 10^5
    There will be at least one element in the data structure before calling findMedian.
    At most 5 * 104 calls will be made to addNum and findMedian.
    """

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        if self.large and num >= self.large[0]:
            heapq.heappush(self.large, num)
            if len(self.large) - len(self.small) >= 2:
                heapq.heappush(self.small, -heapq.heappop(self.large))
        else:
            heapq.heappush(self.small, -num)
            if len(self.small) - len(self.large) >= 2:
                heapq.heappush(self.large, -heapq.heappop(self.small))

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (self.large[0] - self.small[0]) / 2
        elif len(self.small) > len(self.large):
            return -self.small[0]
        else:
            return self.large[0]


def test():
    finder = MedianFinder()
    finder.addNum(1)
    assert finder.findMedian() == 1.0
    finder.addNum(2)
    finder.addNum(3)
    assert finder.findMedian() == 2.0
    finder.addNum(4)
    finder.addNum(5)
    finder.addNum(6)
    finder.addNum(7)
    finder.addNum(8)
    finder.addNum(9)
    finder.addNum(10)
    assert finder.findMedian() == 5.5


if __name__ == '__main__':
    test()
