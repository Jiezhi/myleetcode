#!/usr/bin/env python3
"""
CREATED AT: 2022-07-05

URL: https://leetcode.com/problems/my-calendar-i/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 729-MyCalendarI

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
import bisect


class MyCalendar:
    """
    Runtime: 891 ms, faster than 22.16% 
    Memory Usage: 14.8 MB, less than 59.41% 

    0 <= start < end <= 10^9
    At most 1000 calls will be made to book.
    """

    def __init__(self):
        self.calendar = [(-1, 0)]

    def book(self, start: int, end: int) -> bool:
        pos = bisect.bisect([x[0] for x in self.calendar], start)
        if start < self.calendar[pos - 1][1]:
            return False
        if pos == len(self.calendar):
            if start == self.calendar[pos - 1][1]:
                self.calendar[-1] = (self.calendar[-1][0], end)
            else:
                self.calendar.append((start, end))
        else:
            if end > self.calendar[pos][0]:
                return False
            elif start == self.calendar[pos - 1][1]:
                if end == self.calendar[pos][0]:
                    self.calendar[pos - 1] = (self.calendar[pos - 1][0], self.calendar[pos][1])
                    self.calendar.pop(pos)
                else:
                    self.calendar[pos - 1] = (self.calendar[pos - 1][0], end)
            else:
                if end == self.calendar[pos][0]:
                    self.calendar[pos] = (start, self.calendar[pos][1])
                else:
                    self.calendar.insert(pos, (start, end))
        return True


def test():
    calendar = MyCalendar()
    assert calendar.book(10, 20)
    assert not calendar.book(15, 25)
    assert calendar.book(20, 30)
    assert calendar.book(0, 10)

    calendar = MyCalendar()
    assert calendar.book(47, 50)
    assert calendar.book(33, 41)
    assert not calendar.book(39, 45)


if __name__ == '__main__':
    test()
