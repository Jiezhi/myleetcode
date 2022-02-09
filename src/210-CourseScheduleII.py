#!/usr/bin/env python
"""
CREATED AT: 2021/12/23
Des:

https://leetcode.com/problems/course-schedule-ii/
https://leetcode.com/explore/learn/card/graph/623/kahns-algorithm-for-topological-sorting/3868/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: Graph

See: 

Time Spent: 30 min
"""
import collections
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        CREATED AT: 2022/02/09
        44 / 44 test cases passed.
        Status: Accepted
        Runtime: 204 ms, faster than 14.87%
        Memory Usage: 15.6 MB, less than 64.15%
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
        course_dict = dict()
        for i in range(numCourses):
            course_dict[i] = set()
        course_dict2 = collections.defaultdict(list)
        for courses in prerequisites:
            course_dict[courses[0]].add(courses[1])
            course_dict2[courses[1]].append(courses[0])
        ret = []
        visited = set()
        ret_changed = True
        while len(visited) < numCourses and ret_changed:
            ret_changed = False
            for key, value in course_dict.items():
                if not value and key not in visited:
                    visited.add(key)
                    ret.append(key)
                    ret_changed = True
                    for to_remove in course_dict2[key]:
                        course_dict[to_remove].remove(key)

        return ret if len(ret) == numCourses else []

    def findOrder2(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
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


if __name__ == '__main__':
    test()
