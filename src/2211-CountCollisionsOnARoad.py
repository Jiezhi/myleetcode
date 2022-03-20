#!/usr/bin/env python
"""
CREATED AT: 2022/3/20
Des:

https://leetcode.com/problems/count-collisions-on-a-road/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: Weekly Contest 285

See: 

"""


class Solution:
    def countCollisions2(self, s: str) -> int:
        """
        See https://leetcode-cn.com/problems/count-collisions-on-a-road/solution/zui-duan-dai-ma-bu-jie-shi-by-freeyourmi-6o0r/
        :param s:
        :return:
        """
        return len(s.lstrip('L').rstrip('R')) - s.count('S')

    def countCollisions(self, directions: str) -> int:
        """
        1 <= directions.length <= 10^5
        directions[i] is either 'L', 'R', or 'S'.
        """
        if not directions:
            return 0
        start = 0
        while start < len(directions) and directions[start] == 'L':
            start += 1

        end = len(directions) - 1
        while end > 0 and directions[end] == 'R':
            end -= 1
        if start >= end:
            return 0
        ds = directions[start: end + 1]
        if len(ds) == 1:
            return 0
        pre = ds[0]
        ret = 0
        i = 1
        while i < len(ds):
            d = ds[i]
            if pre == 'S':
                if d == 'L':
                    ret += 1
                elif d == 'R':
                    pre = 'R'
            elif pre == 'R':
                if d == 'S':
                    ret += 1
                    pre = 'S'
                elif d == 'L':
                    ret += 2
                    pre = 'S'
                elif d == 'R':
                    pos = 1
                    while i + pos < len(ds) and ds[i + pos] == 'R':
                        pos += 1
                    if ds[i + pos] == 'L':
                        ret += pos + 2
                        i += pos + 1
                        pre = 'S'
                        continue
                    elif ds[i + pos] == 'S':
                        ret += pos + 1
                        i += pos + 1
                        pre = 'S'
                        continue
            i += 1

        return ret


def test():
    assert Solution().countCollisions("RLRSLL") == 5
    assert Solution().countCollisions2("RLRSLL") == 5
    assert Solution().countCollisions("LLRR") == 0


if __name__ == '__main__':
    test()
