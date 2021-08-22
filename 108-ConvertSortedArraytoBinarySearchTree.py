#!/usr/bin/env python
"""
CREATED AT: 2021/8/20
Des:
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
https://leetcode.com/explore/featured/card/top-interview-questions-easy/94/trees/631/
GITHUB: https://github.com/Jiezhi/myleetcode

"""

from typing import List, Optional

from tree_node import TreeNode, print_tree_node


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """
        31 / 31 test cases passed.
        Status: Accepted
        Runtime: 56 ms
        Memory Usage: 15.7 MB
        :param nums:
        :return:
        """
        n = len(nums)
        if n == 0:
            return None
        if n == 1:
            return TreeNode(val=nums[0])
        mid = n // 2
        root = TreeNode(nums[mid])
        if mid - 1 >= 0:
            root.left = self.sortedArrayToBST(nums[:mid])
        if mid + 1 < n:
            root.right = self.sortedArrayToBST(nums[mid + 1:])
        return root


def test():
    # [0,-3,9,-10,null,5] or [0,-10,5,null,-3,null,9]
    ret = Solution().sortedArrayToBST(nums=[-10, -3, 0, 5, 9])
    print_tree_node(ret)
    # [1,3] or [3,1]
    ret = Solution().sortedArrayToBST(nums=[1, 3])
    print_tree_node(ret)


if __name__ == '__main__':
    test()
