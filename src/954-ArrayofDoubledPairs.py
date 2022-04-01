#!/usr/bin/env python
"""
CREATED AT: 2021/8/11
Des:
https://leetcode.com/problems/array-of-doubled-pairs/
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge-2021/614/week-2-august-8th-august-14th/3877/
GITHUB: https://github.com/Jiezhi/myleetcode

Reference: https://leetcode.com/problems/array-of-doubled-pairs/solution/

"""
import collections
from typing import List


class Solution:
    def canReorderDoubled2(self, arr: List[int]) -> bool:
        """
        Update: 20220401

        Runtime: 596 ms, faster than 97.28%
        Memory Usage: 16.6 MB, less than 62.22%

        :param arr: 2 <= arr.length <= 3 * 10^4
                    arr.length is even.
                    -10^5 <= arr[i] <= 10^5
        :return:
        """
        cnt = collections.Counter(arr)
        if cnt[0] % 2 != 0:
            return False

        for num in sorted(set(arr)):
            if cnt[num] <= 0:
                continue
            if num == 0:
                del cnt[num]
            elif num < 0:
                if num % 2 != 0 or cnt[num // 2] < cnt[num]:
                    return False
                cnt[num // 2] -= cnt[num]
                del cnt[num]
            else:
                if cnt[num * 2] < cnt[num]:
                    return False
                cnt[num * 2] -= cnt[num]
                del cnt[num]
        return True

    def canReorderDoubled(self, arr: List[int]) -> bool:
        """
        102 / 102 test cases passed.
        Status: Accepted
        Runtime: 7000 ms
        Memory Usage: 16.9 MB
        My solution spend too much time at list operations.
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

    assert not Solution().canReorderDoubled2(arr=[3, 1, 3, 6])
    assert not Solution().canReorderDoubled2(arr=[2, 1, 2, 6])
    assert Solution().canReorderDoubled2(arr=[4, -2, 2, -4])
    assert not Solution().canReorderDoubled2(arr=[1, 2, 4, 16, 8, 4])


if __name__ == '__main__':
    test()
