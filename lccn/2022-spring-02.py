#!/usr/bin/env python
"""
CREATED AT: 2022/4/16
Des:
https://leetcode-cn.com/contest/season/2022-spring/problems/WHnhjV/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

DES:
2. 烹饪料理

欢迎各位勇者来到力扣城，城内设有烹饪锅供勇者制作料理，为自己恢复状态。

勇者背包内共有编号为 0 ~ 4 的五种食材，其中 meterials[j] 表示第 j 种食材的数量。通过这些食材可以制作若干料理，cookbooks[i][j] 表示制作第 i 种料理需要第 j 种食材的数量，而 attribute[i] = [x,y] 表示第 i 道料理的美味度 x 和饱腹感 y。

在饱腹感不小于 limit 的情况下，请返回勇者可获得的最大美味度。如果无法满足饱腹感要求，则返回 -1。

注意：

每种料理只能制作一次。
"""
import collections
from typing import List


class Solution:
    def perfectMenu(self, materials: List[int], cookbooks: List[List[int]], attribute: List[List[int]],
                    limit: int) -> int:
        """
        meterials.length == 5
        1 <= cookbooks.length == attribute.length <= 8
        cookbooks[i].length == 5
        attribute[i].length == 2
        0 <= meterials[i], cookbooks[i][j], attribute[i][j] <= 20
        1 <= limit <= 100
        """
        n = len(cookbooks)
        dq = collections.deque()
        dq.append((materials, 1, 0, 0))
        dq.append(([materials[i] - cookbooks[0][i] for i in range(5)], 1, attribute[0][0], attribute[0][1]))
        ret = -1
        while dq:
            mat, pos, cnt, lim = dq.popleft()
            if any(x < 0 for x in mat) or pos > n:
                continue
            if lim >= limit:
                ret = max(ret, cnt)
            if pos == n:
                continue
            dq.append(([mat[i] - cookbooks[pos][i] for i in range(5)], pos + 1, cnt + attribute[pos][0],
                       lim + attribute[pos][1]))
            dq.append((mat, pos + 1, cnt, lim))
        return ret


def test():
    assert Solution().perfectMenu(materials=[3, 2, 4, 1, 2],
                                  cookbooks=[[1, 1, 0, 1, 2], [2, 1, 4, 0, 0], [3, 2, 4, 1, 0]],
                                  attribute=[[3, 2], [2, 4], [7, 6]],
                                  limit=5) == 7


if __name__ == '__main__':
    test()
