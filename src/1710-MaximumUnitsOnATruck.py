#!/usr/bin/env python3
"""
CREATED AT: 2022-07-01

URL: https://leetcode.com/problems/maximum-units-on-a-truck/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1710-MaximumUnitsOnATruck

Difficulty: Easy

Desc: 

Tag: 

See: 

"""
from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        """
        Runtime: 194 ms, faster than 72.50%
        Memory Usage: 14.4 MB, less than 32.64%

        1 <= boxTypes.length <= 1000
        1 <= numberOfBoxesi, numberOfUnitsPerBoxi <= 1000
        1 <= truckSize <= 10^6
        """
        box = sorted(boxTypes, key=lambda x: [-x[1], x[0]])
        ret, pos = 0, 0
        while truckSize > 0 and pos < len(box):
            if truckSize >= box[pos][0]:
                truckSize -= box[pos][0]
                ret += box[pos][0] * box[pos][1]
                pos += 1
            else:
                ret += truckSize * box[pos][1]
                break
        return ret


def test():
    assert Solution().maximumUnits(boxTypes=[[1, 3], [2, 2], [3, 1]], truckSize=4) == 8
    assert Solution().maximumUnits(boxTypes=[[5, 10], [2, 5], [4, 7], [3, 9]], truckSize=10) == 91


if __name__ == '__main__':
    test()
