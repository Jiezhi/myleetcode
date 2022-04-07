#!/usr/bin/env python
"""
CREATED AT: 2022/4/7
Des:
https://leetcode.com/problems/seat-reservation-manager/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""
import heapq


class SeatManager:
    """
    Runtime: 588 ms, faster than 87.99%
    Memory Usage: 42 MB, less than 22.71%

    1 <= n <= 10^5
    1 <= seatNumber <= n
    For each call to reserve, it is guaranteed that there will be at least one unreserved seat.
    For each call to unreserve, it is guaranteed that seatNumber will be reserved.
    At most 105 calls in total will be made to reserve and unreserve.
    """

    def __init__(self, n: int):
        self.seats = [i for i in range(1, n + 1)]

    def reserve(self) -> int:
        return heapq.heappop(self.seats)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.seats, seatNumber)


def test():
    seatManager = SeatManager(10)
    assert seatManager.reserve() == 1
    assert seatManager.reserve() == 2
    assert seatManager.reserve() == 3
    seatManager.unreserve(2)
    assert seatManager.reserve() == 2


if __name__ == '__main__':
    test()
