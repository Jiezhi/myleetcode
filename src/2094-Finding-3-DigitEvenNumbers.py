#!/usr/bin/env python
"""
CREATED AT: 2021/12/5
Des:

https://leetcode.com/problems/finding-3-digit-even-numbers
https://leetcode.com/contest/weekly-contest-270/problems/finding-3-digit-even-numbers/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 
"""
from typing import List


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        """
        3 <= digits.length <= 100
        0 <= digits[i] <= 9
        :param digits:
        :return:
        """
        ret_set = set()
        for i in range(len(digits)):
            if digits[i] % 2 == 0:
                for j in range(len(digits)):
                    if j == i or digits[j] == 0:
                        continue
                    for k in range(len(digits)):
                        if k == i or k == j:
                            continue
                        ret_set.add(digits[j] * 100 + digits[k] * 10 + digits[i])
            else:
                continue
        return sorted(list(ret_set))


def test():
    assert Solution().findEvenNumbers(digits=[2, 1, 3, 0]) == [102, 120, 130, 132, 210, 230, 302, 310, 312, 320]
    assert Solution().findEvenNumbers(digits=[2, 2, 8, 8, 2]) == [222, 228, 282, 288, 822, 828, 882]
    assert Solution().findEvenNumbers(digits=[3, 7, 5]) == []
    assert Solution().findEvenNumbers(digits=[0, 2, 0, 0]) == [200]
    assert Solution().findEvenNumbers(digits=[0, 0, 0]) == []


if __name__ == '__main__':
    test()
