#!/usr/bin/env python3
"""
CREATED AT: 2022-09-09

URL: https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1996-TheNumberOfWeakCharactersInTheGame

Difficulty: Medium

Desc: 

Tag: 

See: https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/discuss/2551739/LeetCode-The-Hard-Way-Line-By-Line-Explanation
Not use heap

"""
from tool import *


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        """
        Modified list sort, and reduce heap size
        Runtime: 4435 ms, faster than 15.08%
        Memory Usage: 68.3 MB, less than 23.33%

        2 <= properties.length <= 10^5
        properties[i].length == 2
        1 <= attacki, defensei <= 10^5
        """
        properties.sort(key=operator.itemgetter(0, 1))

        ret = 0

        hq = [(-properties[-1][1], properties[-1][0])]
        pre = properties[0]
        for cur in properties:
            if cur[0] != pre[0]:
                heapq.heappush(hq, (-pre[1], pre[0]))
            pre = cur

        for a, d in properties:
            while hq and hq[0][1] <= a:
                heapq.heappop(hq)
            if not hq:
                break
            if -hq[0][0] > d:
                ret += 1
        return ret

    def numberOfWeakCharacters2(self, properties: List[List[int]]) -> int:
        """
        Runtime: 6142 ms, faster than 5.04%
        Memory Usage: 68.2 MB, less than 29.64%

        2 <= properties.length <= 10^5
        properties[i].length == 2
        1 <= attacki, defensei <= 10^5
        """
        properties.sort(key=lambda x: (x[0], x[1]))

        ret = 0

        hq = [(-x[1], x[0]) for x in properties]
        heapq.heapify(hq)

        for a, d in properties:
            while hq and hq[0][1] <= a:
                heapq.heappop(hq)
            if not hq:
                break
            if -hq[0][0] > d:
                ret += 1
        return ret


def test():
    assert Solution().numberOfWeakCharacters(properties=[[7, 9], [10, 7], [6, 9], [10, 4], [7, 5], [7, 10]]) == 2
    assert Solution().numberOfWeakCharacters(properties=[[5, 5], [6, 3], [3, 6]]) == 0
    assert Solution().numberOfWeakCharacters(properties=[[2, 2], [3, 3]]) == 1
    assert Solution().numberOfWeakCharacters(properties=[[1, 5], [10, 4], [4, 3]]) == 1


if __name__ == '__main__':
    test()
