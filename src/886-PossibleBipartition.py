#!/usr/bin/env python3
"""
CREATED AT: 2022-10-17

URL: https://leetcode.com/problems/possible-bipartition/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 886-PossibleBipartition

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        """
        Runtime: 747 ms, faster than 91.87%
        Memory Usage: 20.9 MB, less than 54.93%

        1 <= n <= 2000
        0 <= dislikes.length <= 10^4
        dislikes[i].length == 2
        1 <= dislikes[i][j] <= n
        ai < bi
        All the pairs of dislikes are unique.
        """

        cnt = Counter()
        adj = collections.defaultdict(set)
        for a, b in dislikes:
            adj[b].add(a)
            adj[a].add(b)
            cnt[b] += 1

        set1, set2 = set(), set()
        while len(cnt) > 0:
            node = cnt.most_common(1)
            dq = deque([(node[0][0], 1)])
            while dq:
                num, set_type = dq.popleft()
                if set_type == 1:
                    if num in set1:
                        continue
                    if num in set2:
                        return False
                    set1.add(num)
                else:
                    if num in set2:
                        continue
                    if num in set1:
                        return False
                    set2.add(num)
                for b in adj[num]:
                    dq.append((b, -set_type))
                del cnt[num]
        return True


def test():
    assert Solution().possibleBipartition(n=4, dislikes=[[1, 2], [1, 3], [2, 4]])
    assert not Solution().possibleBipartition(n=3, dislikes=[[1, 2], [1, 3], [2, 3]])
    assert not Solution().possibleBipartition(n=5, dislikes=[[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]])


if __name__ == '__main__':
    test()
