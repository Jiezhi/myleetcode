#!/usr/bin/env python3
"""
CREATED AT: 2022-06-29

URL: https://leetcode.com/problems/queue-reconstruction-by-height/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 406-QueueReconstructionByHeight

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
import collections
from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        """
        Runtime: 515 ms, faster than 17.77% 
        Memory Usage: 14.6 MB, less than 14.52% 

        1 <= people.length <= 2000
        0 <= hi <= 10^6
        0 <= ki < people.length
        It is guaranteed that the queue can be reconstructed.
        """
        cnt = collections.defaultdict(list)
        for k, v in people:
            cnt[v].append(k)

        ret = []

        for v in sorted(cnt.keys()):
            for k in sorted(cnt[v], reverse=True):
                if not ret:
                    ret.append([k, v])
                    continue
                i, j = 0, v
                while j > 0:
                    if ret[i][0] >= k:
                        j -= 1
                    i += 1
                ret.insert(i, [k, v])
        return ret


def test():
    assert Solution().reconstructQueue(
        people=[[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    ) == [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]
    assert Solution().reconstructQueue(
        people=[[6, 0], [5, 0], [4, 0], [3, 2], [2, 2], [1, 4]]
    ) == [[4, 0], [5, 0], [2, 2], [3, 2], [1, 4], [6, 0]]


if __name__ == '__main__':
    test()
