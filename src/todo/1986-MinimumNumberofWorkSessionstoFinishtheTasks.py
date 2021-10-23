#!/usr/bin/env python
"""
CREATED AT: 2021/8/29
Des:
https://leetcode.com/problems/minimum-number-of-work-sessions-to-finish-the-tasks
https://leetcode.com/contest/weekly-contest-256/problems/minimum-number-of-work-sessions-to-finish-the-tasks/
GITHUB: https://github.com/Jiezhi/myleetcode

"""
from typing import List


class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        cnt = 0
        tasks = sorted(tasks, reverse=True)

        while len(tasks) > 0:
            if tasks[0] == sessionTime:
                tasks.remove(tasks[0])
                cnt += 1
                continue
            if len(tasks) == 1:
                cnt += 1
                break
            left = sessionTime - tasks[0]
            tasks.remove(tasks[0])
            if left in tasks:
                tasks.remove(left)
                cnt += 1
            else:
                to_remove = []
                for task in tasks:
                    if task <= left:
                        left -= task
                        to_remove.append(task)
                for r in to_remove:
                    tasks.remove(r)
                cnt += 1

        return cnt


def test():
    assert Solution().minSessions(tasks=[2, 3, 3, 4, 4, 4, 5, 6, 7, 10], sessionTime=12) == 4
    assert Solution().minSessions(tasks=[1], sessionTime=2) == 1
    assert Solution().minSessions(tasks=[1, 2, 3], sessionTime=3) == 2
    assert Solution().minSessions(tasks=[3, 1, 3, 1, 1], sessionTime=8) == 2
    assert Solution().minSessions(tasks=[1, 2, 3, 4, 5], sessionTime=15) == 1


if __name__ == '__main__':
    test()
