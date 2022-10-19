#!/usr/bin/env python3
"""
CREATED AT: 2022-10-19

URL: https://leetcode.com/problems/reconstruct-itinerary/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 332-ReconstructItinerary

Difficulty: Hard

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """
        https://leetcode.cn/problems/reconstruct-itinerary/solution/zhong-xin-an-pai-xing-cheng-by-leetcode-solution/
        Hierholzer
        """
        adj = collections.defaultdict(list)
        for a, b in tickets:
            adj[a].append(b)
        for k in adj.keys():
            adj[k] = sorted(adj[k], reverse=True)
        ret = []

        def dfs(node):
            while adj[node]:
                dfs(adj[node].pop())
            ret.append(node)

        dfs('JFK')
        return ret[::-1]

    def findItinerary2(self, tickets: List[List[str]]) -> List[str]:
        """
        Runtime: 998 ms, faster than 5.04%
        Memory Usage: 35.7 MB, less than 7.12%

        1 <= tickets.length <= 300
        tickets[i].length == 2
        fromi.length == 3
        toi.length == 3
        fromi and toi consist of uppercase English letters.
        fromi != toi
        """
        adj = collections.defaultdict(list)
        cnt = Counter()
        for a, b in tickets:
            adj[a].append(b)
            cnt[(a, b)] += 1
        for k in adj.keys():
            adj[k] = sorted(adj[k], reverse=True)

        stack = [(['JFK'], cnt)]
        while stack:
            ret, cnt = stack.pop()
            if len(ret) == len(tickets) + 1:
                return ret
            k = ret[-1]
            for v in adj[k]:
                if cnt[(k, v)] <= 0:
                    continue
                retcopy = ret.copy()
                ccopy = cnt.copy()
                ccopy[(k, v)] -= 1
                retcopy.append(v)
                stack.append((retcopy, ccopy))


def test():
    tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    answer = ["JFK", "MUC", "LHR", "SFO", "SJC"]

    assert Solution().findItinerary(tickets=tickets) == answer


if __name__ == '__main__':
    test()
