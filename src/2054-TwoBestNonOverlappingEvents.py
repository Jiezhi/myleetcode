#!/usr/bin/env python
"""
CREATED AT: 2021/10/30
Des:

https://leetcode.com/problems/two-best-non-overlapping-events/
https://leetcode.com/contest/biweekly-contest-64/problems/two-best-non-overlapping-events/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 
"""
import heapq
from typing import List


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        """
        Runtime: 2230 ms, faster than 67.87%
        Memory Usage: 58 MB, less than 19.22%
        2 <= events.length <= 10^5
        events[i].length == 3
        1 <= startTime_i <= endTime_i <= 10^9
        1 <= value_i <= 10^6
        :param events:
        :return:
        """
        # sort by end time
        events = sorted(events, key=lambda x: x[1])
        end_values = []
        _, pre_end, pre_max_value = events[0]
        for event in events[1:]:
            if event[1] != pre_end:
                end_values.append((pre_end, pre_max_value))
                pre_end = event[1]
            pre_max_value = max(pre_max_value, event[2])

        end_values.append((pre_end, pre_max_value))
        ret = pre_max_value
        heapq.heapify(end_values)
        # sort by start time
        events = sorted(events, key=lambda x: x[0])

        pre_start, pre_end, tmp_max_value = events[0]
        tmp_value = 0
        for event in events[1:]:
            if event[2] > tmp_max_value:
                ret = max(ret, tmp_value + event[2])

            while end_values and event[0] > end_values[0][0]:
                _, tmp_value = heapq.heappop(end_values)
                ret = max(ret, event[2] + tmp_value)

            tmp_max_value = event[2]
        return ret

    def maxTwoEvents2(self, events: List[List[int]]) -> int:
        """
        Memory Limit Exceeded
        2 <= events.length <= 10^5
        events[i].length == 3
        1 <= startTime_i <= endTime_i <= 10^9
        1 <= value_i <= 10^6
        :param events:
        :return:
        """
        max_end = max(x[1] for x in events)

        ts = [0] * (max_end + 1)
        for event in events:
            ts[event[1]] = max(ts[event[1]], event[2])

        for i in range(1, max_end):
            ts[i] = max(ts[i], ts[i - 1])

        ret = ts[-1]

        for event in events:
            ret = max(ret, event[2] + ts[event[0] - 1])
        return ret


def test():
    assert Solution().maxTwoEvents(
        [[66, 97, 90], [98, 98, 68], [38, 49, 63], [91, 100, 42], [92, 100, 22], [1, 77, 50], [64, 72, 97]]) == 165
    assert Solution().maxTwoEvents(events=[[1, 3, 2], [4, 5, 2], [2, 4, 3]]) == 4
    assert Solution().maxTwoEvents(events=[[1, 3, 2], [4, 5, 2], [1, 5, 5]]) == 5
    assert Solution().maxTwoEvents(events=[[1, 5, 3], [1, 5, 1], [6, 6, 5]]) == 8


if __name__ == '__main__':
    test()
