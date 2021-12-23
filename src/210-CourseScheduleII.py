#!/usr/bin/env python
"""
CREATED AT: 2021/12/23
Des:

https://leetcode.com/problems/course-schedule-ii/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

Time Spent: 30 min
"""
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Runtime: 152 ms, faster than 17.37%
        Memory Usage: 19.6 MB, less than 5.80%

        1 <= numCourses <= 2000
        0 <= prerequisites.length <= numCourses * (numCourses - 1)
        prerequisites[i].length == 2
        0 <= ai, bi < numCourses
        ai != bi
        All the pairs [ai, bi] are distinct.
        :param numCourses:
        :param prerequisites:
        :return:
        """
        pre_dict = dict()
        next_dict = dict()
        for prereq in prerequisites:
            if prereq[0] not in pre_dict:
                pre_dict[prereq[0]] = set()
            pre_dict[prereq[0]].add(prereq[1])

            if prereq[1] not in next_dict:
                next_dict[prereq[1]] = set()
            next_dict[prereq[1]].add(prereq[0])
        ret = []

        def dfs(course: int):
            nonlocal ret
            nonlocal pre_dict
            nonlocal next_dict
            if course in ret:
                return
            if course not in pre_dict:
                # course have no prerequisites, just take it
                ret.append(course)
                if course in next_dict:
                    next_list = next_dict[course]
                    for next in next_list:
                        if next in pre_dict:
                            pre_dict[next].remove(course)
                            if not pre_dict[next]:
                                pre_dict.pop(next)
                                dfs(next)

        for i in range(numCourses):
            dfs(i)
        return ret if len(ret) == numCourses else []


def test():
    assert Solution().findOrder(numCourses=2, prerequisites=[[0, 1], [1, 0]]) == []
    assert Solution().findOrder(numCourses=3, prerequisites=[[0, 1], [1, 2], [2, 0]]) == []
    assert Solution().findOrder(numCourses=4, prerequisites=[[1, 2], [2, 3], [3, 1]]) == []
    assert Solution().findOrder(numCourses=2, prerequisites=[[1, 0]]) == [0, 1]
    assert Solution().findOrder(numCourses=1, prerequisites=[]) == [0]
    ret = [[0, 1, 2, 3], [0, 2, 1, 3]]
    assert Solution().findOrder(numCourses=4, prerequisites=[[1, 0], [2, 0], [3, 1], [3, 2]]) in ret

    ret = Solution().findOrder(numCourses=6, prerequisites=[[1, 2], [3, 2], [2, 4], [5, 2], [3, 5], [0, 3]])
    print(ret)


if __name__ == '__main__':
    test()
