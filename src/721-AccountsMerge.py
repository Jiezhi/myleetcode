#!/usr/bin/env python
"""
CREATED AT: 2021/11/29
Des:

GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 
"""
import collections
from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        """
        Runtime: 4052 ms, faster than 5.01%
        Memory Usage: 18.4 MB, less than 68.22%
        1 <= accounts.length <= 1000
        2 <= accounts[i].length <= 10
        1 <= accounts[i][j] <= 30
        accounts[i][0] consists of English letters.
        accounts[i][j] (for j > 0) is a valid email.
        :param accounts:
        :return:
        """
        act_map = [[] for _ in range(len(accounts))]
        for i in range(len(accounts) - 1):
            for j in range(i + 1, len(accounts)):
                if accounts[i][0] == accounts[j][0]:
                    for mail in accounts[j][1:]:
                        if mail in accounts[i][1:]:
                            act_map[i].append(j)
                            act_map[j].append(i)
                            break

        for i in range(len(act_map)):
            if act_map[i]:
                dq = collections.deque()
                for idx in act_map[i]:
                    dq.append(idx)
                act_map[i].clear()
                while len(dq) > 0:
                    tmp_idx = dq.pop()
                    if tmp_idx == i:
                        continue
                    for mail in accounts[tmp_idx][1:]:
                        accounts[i].append(mail)
                    accounts[tmp_idx].clear()
                    for idx in act_map[tmp_idx]:
                        dq.append(idx)
                    act_map[tmp_idx].clear()

        rets = []
        for act in accounts:
            if act:
                ret = sorted(set(act[1:]))
                ret.insert(0, act[0])
                rets.append(ret)
        return rets


def test():
    assert Solution().accountsMerge(
        [["David", "David0@m.co", "David1@m.co"], ["David", "David3@m.co", "David4@m.co"],
         ["David", "David4@m.co", "David5@m.co"], ["David", "David2@m.co", "David3@m.co"],
         ["David", "David1@m.co", "David2@m.co"]]
    ) == [["David", "David0@m.co", "David1@m.co", "David2@m.co", "David3@m.co", "David4@m.co", "David5@m.co"]]
    ret = Solution().accountsMerge(
        accounts=[["John", "johnsmith@mail.com", "john_newyork@mail.com"],
                  ["John", "johnsmith@mail.com", "john00@mail.com"],
                  ["Mary", "mary@mail.com"], ["John", "johnnybravo@mail.com"]]
    )
    ans = [["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"],
           ["Mary", "mary@mail.com"],
           ["John", "johnnybravo@mail.com"]]
    assert len(ret) == len(ans)
    for a in ans:
        assert a in ret

    ret = Solution().accountsMerge(
        accounts=[["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe1@m.co"],
                  ["Kevin", "Kevin3@m.co", "Kevin5@m.co", "Kevin0@m.co"],
                  ["Ethan", "Ethan5@m.co", "Ethan4@m.co", "Ethan0@m.co"],
                  ["Hanzo", "Hanzo3@m.co", "Hanzo1@m.co", "Hanzo0@m.co"],
                  ["Fern", "Fern5@m.co", "Fern1@m.co", "Fern0@m.co"]]
    )
    ans = [["Ethan", "Ethan0@m.co", "Ethan4@m.co", "Ethan5@m.co"], ["Gabe", "Gabe0@m.co", "Gabe1@m.co", "Gabe3@m.co"],
           ["Hanzo", "Hanzo0@m.co", "Hanzo1@m.co", "Hanzo3@m.co"],
           ["Kevin", "Kevin0@m.co", "Kevin3@m.co", "Kevin5@m.co"], ["Fern", "Fern0@m.co", "Fern1@m.co", "Fern5@m.co"]]
    assert len(ret) == len(ans)
    for a in ans:
        assert a in ret


if __name__ == '__main__':
    test()
