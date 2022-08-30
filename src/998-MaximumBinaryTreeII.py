#!/usr/bin/env python3
"""
CREATED AT: 2022-08-30

URL: https://leetcode.com/problems/maximum-binary-tree-ii/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 998-MaximumBinaryTreeII

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from tool import *
from tree_node import TreeNode


class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        Runtime: 29 ms, faster than 98.45%
        Memory Usage: 13.9 MB, less than 86.01%

        The number of nodes in the tree is in the range [1, 100].
        1 <= Node.val <= 100
        All the values of the tree are unique.
        1 <= val <= 100
        """
        if not root or val > root.val:
            return TreeNode(val, root)
        root.right = self.insertIntoMaxTree(root.right, val)
        return root


def test():
    assert Solution().insertIntoMaxTree(TreeNode.from_list([4, 1, 3, null, null, 2]), val=5) == TreeNode.from_list(
        [5, 4, null, 1, 3, null, null, 2])
    assert Solution().insertIntoMaxTree(TreeNode.from_list([5, 2, 4, null, 1]), val=3) == TreeNode.from_list(
        [5, 2, 4, null, 1, null, 3])


if __name__ == '__main__':
    test()
