#!/usr/bin/env python
"""
Github: https://github.com/Jiezhi/myleetcode

Created on 2019/10/17

Leetcode: https://leetcode.com/problems/daily-temperatures/

https://leetcode.com/explore/learn/card/queue-stack/230/usage-stack/1363/

Difficulty: Medium

"""
from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ret = []
        for i in range(len(T) - 1):
            found = False
            for j in range(i + 1, len(T)):
                if T[i] < T[j]:
                    ret.append(j - i)
                    found = True
                    break
            if not found:
                ret.append(0)
        ret.append(0)
        return ret

    def dailyTemperatures2(self, temperatures: List[int]) -> List[int]:
        """
        Runtime: 1239 ms, faster than 67.44%
        Memory Usage: 24.4 MB, less than 97.35%
        如果顺序处理，虽然能得出结果，但肯定超时
        所以要反过来处理，通过观测可以发现，如果当前处理的数 T[i]大于后面比较的数T[j]，则可以直接比较T[j]对应的结果 s 个位数后的结果 T[j+s]
        此外，可以用一个变量标识当前处理数T[i]右边最大的数max，如果 T[i] >= max，那么 T[i] 对应的数肯定是0了。
        :param temperatures:
        :return:
        """
        ret = [0]
        l = len(temperatures)
        for i in range(l - 2, -1, -1):
            j = i + 1
            while j <= l:
                if temperatures[j] > temperatures[i]:
                    ret.append(j - i)
                    break
                elif ret[l - j - 1] == 0:
                    ret.append(0)
                    break
                else:
                    j += ret[l - j - 1]
        ret.reverse()
        return ret


def test():
    assert Solution().dailyTemperatures2([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]


if __name__ == '__main__':
    test()
