#!/usr/bin/env python
"""
CREATED AT: 2022/3/3
Des:

https://leetcode.com/problems/course-schedule/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

Time Spent:  min
"""
import collections
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Ref: https://leetcode.com/problems/course-schedule/discuss/162743/JavaC%2B%2BPython-BFS-Topological-Sorting-O(N-%2B-E)
        Runtime: 147 ms, faster than 49.82%
        Memory Usage: 15.5 MB, less than 75.15%

        1 <= numCourses <= 10^5
        0 <= prerequisites.length <= 5000
        prerequisites[i].length == 2
        0 <= ai, bi < numCourses
        All the pairs prerequisites[i] are unique.
        """
        # check the graph has circle or not
        G = [[] for _ in range(numCourses)]
        degrees = [0] * numCourses
        for course, pre_course in prerequisites:
            G[course].append(pre_course)
            degrees[pre_course] += 1

        dq = collections.deque(i for i in range(numCourses) if degrees[i] == 0)

        while dq:
            pre_course = dq.popleft()
            for course in G[pre_course]:
                degrees[course] -= 1
                if degrees[course] == 0:
                    dq.append(course)
        return False if any(x > 0 for x in degrees) else True

    def canFinish2(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Runtime: 302 ms, faster than 7.10%
        Memory Usage: 15.6 MB, less than 68.77%

        1 <= numCourses <= 10^5
        0 <= prerequisites.length <= 5000
        prerequisites[i].length == 2
        0 <= ai, bi < numCourses
        All the pairs prerequisites[i] are unique.
        """
        # check the graph has circle or not
        course_dict = collections.defaultdict(set)
        pre_course_dict = collections.defaultdict(set)
        for course, pre_course in prerequisites:
            course_dict[course].add(pre_course)
            pre_course_dict[pre_course].add(course)

        pre_len = 0
        curr_len = len(pre_course_dict)
        while pre_len != curr_len:
            pre_len = curr_len
            course_to_remove = None
            for key in pre_course_dict.keys():
                if not course_dict[key]:
                    # course[key] no prerequisite courses
                    for value in pre_course_dict[key]:
                        course_dict[value].remove(key)
                    course_to_remove = key
                    break
            if course_to_remove is not None:
                del pre_course_dict[key]

            curr_len = len(pre_course_dict)

        return True if len(pre_course_dict) == 0 else False


def test():
    assert Solution().canFinish(numCourses=2, prerequisites=[[1, 0]])
    assert not Solution().canFinish(numCourses=2, prerequisites=[[1, 0], [0, 1]])

    assert Solution().canFinish2(numCourses=2, prerequisites=[[1, 0]])
    assert not Solution().canFinish2(numCourses=2, prerequisites=[[1, 0], [0, 1]])


if __name__ == '__main__':
    test()
