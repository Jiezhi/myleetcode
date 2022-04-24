#!/usr/bin/env python
"""
CREATED AT: 2022/4/24
Des:

GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""
import collections


class UndergroundSystem:
    """
    Runtime: 256 ms, faster than 80.03%
    Memory Usage: 23.8 MB, less than 92.27%

    1 <= id, t <= 10^6
    1 <= stationName.length, startStation.length, endStation.length <= 10
    All strings consist of uppercase and lowercase English letters and digits.
    There will be at most 2 * 10^4 calls in total to checkIn, checkOut, and getAverageTime.
    Answers within 10^-5 of the actual value will be accepted.
    """

    def __init__(self):
        self.pair = collections.defaultdict(tuple)
        self.checkin = dict()

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        key = f'{self.checkin[id][0]}-{stationName}'
        pre_sum, pre_cnt = self.pair[key] if key in self.pair else (0, 0)
        self.pair[key] = (pre_sum + t - self.checkin[id][1], pre_cnt + 1)
        del self.checkin[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = f'{startStation}-{endStation}'
        if key not in self.pair or not self.pair[key]:
            return -1
        return self.pair[key][0] / self.pair[key][1]


def test():
    system = UndergroundSystem()
    system.checkIn(45, "Leyton", 3)
    system.checkIn(32, "Paradise", 8)
    system.checkIn(27, "Leyton", 10)
    system.checkOut(45, "Waterloo", 15)
    system.checkOut(27, "Waterloo", 20)
    system.checkOut(32, "Cambridge", 22)
    assert system.getAverageTime("Leyton", "Waterloo") == 11.0


if __name__ == '__main__':
    test()
