#!/usr/bin/env python3
"""
CREATED AT: 2022-10-27

URL: https://leetcode.com/problems/image-overlap/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 835-ImageOverlap

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        """
        Runtime: 1846 ms, faster than 30.99%
        Memory Usage: 13.9 MB, less than 98.25%
        n == img1.length == img1[i].length
        n == img2.length == img2[i].length
        1 <= n <= 30
        img1[i][j] is either 0 or 1.
        img2[i][j] is either 0 or 1.
        """
        max_ret = min(sum(sum(x) for x in img1), sum(sum(y) for y in img2))
        if max_ret <= 1:
            return max_ret
        n, ret = len(img1), 0
        for dx in range(-n, n):
            for dy in range(-n, n):
                tmp = 0
                for i in range(n):
                    if i + dx < 0:
                        continue
                    if i + dx >= n:
                        break
                    for j in range(n):
                        if j + dy < 0:
                            continue
                        if j + dy >= n:
                            break
                        if img1[i][j] == img2[i + dx][j + dy] == 1:
                            tmp += 1
                ret = max(tmp, ret)
                if ret == max_ret:
                    print(dx, dy)
                    return ret
        return ret


def test():
    assert Solution().largestOverlap(img1=[[0, 1], [1, 1]], img2=[[1, 1], [1, 0]]) == 2
    assert Solution().largestOverlap(img1=[[1, 1, 0], [0, 1, 0], [0, 1, 0]],
                                     img2=[[0, 0, 0], [0, 1, 1], [0, 0, 1]]) == 3
    assert Solution().largestOverlap(img1=[[1]], img2=[[1]]) == 1
    assert Solution().largestOverlap(img1=[[0]], img2=[[0]]) == 0


if __name__ == '__main__':
    test()
