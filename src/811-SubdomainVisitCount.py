#!/usr/bin/env python
"""
CREATED AT: 2022/4/21
Des:
https://leetcode.com/problems/subdomain-visit-count/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""
import collections
from typing import List

from tool import equal_list_value


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        """
        Runtime: 79 ms, faster than 41.83%
        Memory Usage: 13.9 MB, less than 42.6%

        1 <= cpdomain.length <= 100
        1 <= cpdomain[i].length <= 100
        cpdomain[i] follows either the "repi d1i.d2i.d3i" format or the "repi d1i.d2i" format.
        repi is an integer in the range [1, 104].
        d1i, d2i, and d3i consist of lowercase English letters.
        """
        cnt = collections.defaultdict(int)
        for domain in cpdomains:
            c, v = domain.split(' ')
            c = int(c)
            ds = v.split('.')
            cnt[v] += c
            cnt[ds[-1]] += c
            if len(ds) == 3:
                cnt[f'{ds[1]}.{ds[2]}'] += c
        ret = []
        for k, v in cnt.items():
            ret.append(f'{v} {k}')
        return ret


def test():
    assert equal_list_value(Solution().subdomainVisits(["9001 discuss.leetcode.com"]),
                            ["9001 discuss.leetcode.com",
                             "9001 leetcode.com",
                             "9001 com"])


if __name__ == '__main__':
    test()
