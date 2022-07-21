#!/usr/bin/env python3
"""
CREATED AT: 2022-07-21

URL: https://leetcode.com/problems/binary-tree-pruning/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 814-BinaryTreePruning

Difficulty: Medium

Desc: 

Tag: 

See: 

"""

from tool import *
from tree_node import TreeNode


class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Runtime: 56 ms, faster than 33.85%
        Memory Usage: 14 MB, less than 26.06%
        The number of nodes in the tree is in the range [1, 200].
        Node.val is either 0 or 1.
        """

        def dfs(node: Optional[TreeNode]) -> bool:
            if not node:
                return False
            contain = False
            if dfs(node.left):
                contain = True
            else:
                node.left = None
            if dfs(node.right):
                contain = True
            else:
                node.right = None
            if not contain and node.val == 0:
                return False
            return True

        return root if dfs(root) else None


def test():
    assert Solution().pruneTree(root=TreeNode.from_list([1, null, 0, 0, 1])) == TreeNode.from_list(
        [1, null, 0, null, 1])
    assert Solution().pruneTree(root=TreeNode.from_list([1, 0, 1, 0, 0, 0, 1])) == TreeNode.from_list(
        [1, null, 1, null, 1])
    assert Solution().pruneTree(root=TreeNode.from_list([1, 0, 0, 0, 0, 0, 0, 0])) == TreeNode.from_list(
        [1])
    assert Solution().pruneTree(root=TreeNode.from_list([0, 0, 0])) == TreeNode.from_list(
        [])


if __name__ == '__main__':
    test()
