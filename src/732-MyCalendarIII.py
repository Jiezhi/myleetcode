#!/usr/bin/env python
"""
CREATED AT: 2022-06-06
Des: https://leetcode.com/problems/my-calendar-iii/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Hard

Tag: 

See: 

"""
import bisect
import collections


class MyCalendarThree:
    """
    Ref: https://leetcode.com/problems/my-calendar-iii/solution/
    Runtime: 3286 ms, faster than 11.53%
    Memory Usage: 14.3 MB, less than 60.32%
    At most 400 calls will be made to book.
    """

    def __init__(self):
        self.cnt = collections.Counter()

    def book(self, start: int, end: int) -> int:
        """

        :param start:
        :param end:
         0 <= start < end <= 10^9
        :return:
        """
        self.cnt[start] += 1
        self.cnt[end] -= 1

        acc, ret = 0, 0
        for x in sorted(self.cnt):
            acc += self.cnt[x]
            ret = max(ret, acc)
        return ret


class MyCalendarThree2:
    """
    FIXME: need to fix the issue
    """

    def __init__(self):
        self.k = 0
        self.bookings = [[-1, 10 ** 9 + 1, 0]]

    def book(self, start: int, end: int) -> int:
        pos = bisect.bisect(list(x[1] for x in self.bookings), end)
        if end != self.bookings[pos][1]:
            self.bookings.insert(pos + 1, [end, self.bookings[pos][1], self.bookings[pos][2]])
            self.bookings[pos] = ([self.bookings[pos][0], end, self.bookings[pos][2]])
            self.k = max(self.k, self.bookings[pos][2])

        while start <= self.bookings[pos][0]:
            self.bookings[pos][2] += 1
            self.k = max(self.k, self.bookings[pos][2])
            pos -= 1

        if start != self.bookings[pos][1]:
            self.bookings.insert(pos + 1, [start, self.bookings[pos][1], self.bookings[pos][2]])
            self.bookings[pos] = [self.bookings[pos][0], start, self.bookings[pos][2] - 1]

        return self.k


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)


def test():
    calendar = MyCalendarThree()
    assert calendar.book(10, 20) == 1
    assert calendar.book(50, 60) == 1
    assert calendar.book(10, 40) == 2
    assert calendar.book(5, 15) == 3
    assert calendar.book(5, 10) == 3
    assert calendar.book(25, 55) == 3


if __name__ == '__main__':
    test()
