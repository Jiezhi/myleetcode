#!/usr/bin/env python
"""
CREATED AT: 2022/4/27
Des:
https://leetcode.com/problems/keys-and-rooms/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""
import collections
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        """
        Runtime: 70 ms, faster than 80.98%
        Memory Usage: 14.5 MB, less than 54.39%
        n == rooms.length
        2 <= n <= 1000
        0 <= rooms[i].length <= 1000
        1 <= sum(rooms[i].length) <= 3000
        0 <= rooms[i][j] < n
        All the values of rooms[i] are unique.
        """
        seen = {0}
        dq = collections.deque([rooms[0]])
        while dq:
            keys = dq.popleft()
            for k in keys:
                if k in seen:
                    continue
                seen.add(k)
                dq.append(rooms[k])
        return len(seen) == len(rooms)


def test():
    assert Solution().canVisitAllRooms([[1], [2], [3], []])
    assert not Solution().canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]])


if __name__ == '__main__':
    test()
