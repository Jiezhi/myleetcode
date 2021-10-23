#!/usr/bin/env python
"""
Created on 2020/11/29

Des:  https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3237/

"""
from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even_cnt = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                even_cnt += 1
        return even_cnt


def test():
    assert Solution().findNumbers([12, 345, 2, 6, 7896]) == 2
    assert Solution().findNumbers([555, 901, 482, 1771]) == 1


if __name__ == '__main__':
    test()
