#!/usr/bin/env python3
"""
CREATED AT: 2022-08-20

URL: https://leetcode.com/problems/maximum-binary-tree/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 654-MaximumBinaryTree

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from tool import *
from tree_node import TreeNode


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        """
        Runtime: 249 ms, faster than 77.55%
        Memory Usage: 14.6 MB, less than 55.67%

        1 <= nums.length <= 1000
        0 <= nums[i] <= 1000
        All integers in nums are unique.
        """
        if not nums:
            return None
        max_pos = 0
        for i, num in enumerate(nums):
            if num > nums[max_pos]:
                max_pos = i
        return TreeNode(nums[max_pos], left=self.constructMaximumBinaryTree(nums[:max_pos]),
                        right=self.constructMaximumBinaryTree(nums[max_pos + 1:]))


def test():
    assert Solution().constructMaximumBinaryTree(nums=[3, 2, 1, 6, 0, 5]) == TreeNode.from_list(
        [6, 3, 5, null, 2, 0, null, null, 1])
    assert Solution().constructMaximumBinaryTree(nums=[3, 2, 1]) == TreeNode.from_list([3, null, 2, null, 1])


if __name__ == '__main__':
    test()
