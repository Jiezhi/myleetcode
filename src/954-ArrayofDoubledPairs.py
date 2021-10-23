#!/usr/bin/env python
"""
CREATED AT: 2021/8/11
Des:
https://leetcode.com/problems/array-of-doubled-pairs/
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge-2021/614/week-2-august-8th-august-14th/3877/
GITHUB: https://github.com/Jiezhi/myleetcode

Reference: https://leetcode.com/problems/array-of-doubled-pairs/solution/

"""
from typing import List


class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        """
        102 / 102 test cases passed.
        Status: Accepted
        Runtime: 7000 ms
        Memory Usage: 16.9 MB
        My solution is spend two much time at list operations.
        The leetcode solution 1 is:
        ```python
        count = collections.Counter(A)
        for x in sorted(A, key = abs):
            if count[x] == 0: continue
            if count[2*x] == 0: return False
            count[x] -= 1
            count[2*x] -= 1
        ```
        return True
        :param arr:
        :return:
        """
        arr = sorted(arr)
        # we remove two elements in a iteration
        for _ in range(len(arr) // 2):
            i = arr.pop(0)
            if i < 0:
                m, n = divmod(i, 2)
                if n == 1 or m not in arr:
                    return False
                else:
                    arr.remove(m)
            else:
                if 2 * i not in arr:
                    return False
                else:
                    arr.remove(2 * i)
        return True


def test():
    assert not Solution().canReorderDoubled(arr=[3, 1, 3, 6])
    assert not Solution().canReorderDoubled(arr=[2, 1, 2, 6])
    assert Solution().canReorderDoubled(arr=[4, -2, 2, -4])
    assert not Solution().canReorderDoubled(arr=[1, 2, 4, 16, 8, 4])


if __name__ == '__main__':
    test()
