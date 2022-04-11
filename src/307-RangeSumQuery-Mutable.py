#!/usr/bin/env python
"""
CREATED AT: 2022/4/11
Des:
https://leetcode.com/problems/range-sum-query-mutable/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 303
Bit Operation for tree: https://leetcode.com/problems/range-sum-query-mutable/discuss/75784/Python:-Well-commented-solution-using-Segment-Trees/221486

"""
from typing import List


class NumArray:
    """
    Runtime: 2412 ms, faster than 63.66%
    Memory Usage: 31.4 MB, less than 59.12%

    1 <= nums.length <= 3 * 10^4
    -100 <= nums[i] <= 100
    0 <= index < nums.length
    -100 <= val <= 100
    0 <= left <= right < nums.length
    At most 3 * 10^4 calls will be made to update and sumRange.
    """

    def _build(self, pos: int) -> int:
        # leaf node
        if pos >= self.n * 2:
            return 0
        self.num_tree[pos] += self._build(2 * pos + 1) + self._build(2 * pos + 2)
        return self.num_tree[pos]

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.num_tree = [0] * len(nums) + nums
        self._build(0)

    def update(self, index: int, val: int) -> None:
        pos = self.n + index
        diff = self.num_tree[pos] - val
        while pos >= 0:
            self.num_tree[pos] -= diff
            pos = (pos - 1) // 2

    def sumRange(self, left: int, right: int) -> int:
        left += self.n
        right += self.n
        ret = 0
        while left <= right:
            if left == right:
                ret += self.num_tree[left]
                break
            if left % 2 == 0:
                ret += self.num_tree[left]
                left += 1
            if right % 2 == 1:
                ret += self.num_tree[right]
                right -= 1
            left = (left - 1) // 2
            right = (right - 1) // 2
        return ret


def test():
    num_array = NumArray([1, 3, 5])
    assert num_array.sumRange(0, 2) == 9
    num_array.update(1, 2)
    assert num_array.sumRange(0, 2) == 8

    num_array = NumArray(list(range(3 * 10 ** 4)))
    assert num_array.sumRange(1, 3 * 10 ** 4 - 10) == 449715045


if __name__ == '__main__':
    test()
