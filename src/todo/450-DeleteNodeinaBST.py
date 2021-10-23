#!/usr/bin/env python
"""
CREATED AT: 2021/9/3
Des:
https://leetcode.com/problems/delete-node-in-a-bst/
https://leetcode.com/explore/learn/card/introduction-to-data-structure-binary-search-tree/141/basic-operations-in-a-bst/1006/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium
"""
from typing import Optional

from tree_node import TreeNode, build_tree_node


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def pop_leftmost_node(node: Optional[TreeNode]) -> (TreeNode, int):
            while node is not None:
                pass

        pass


def test():
    null = None
    assert Solution().deleteNode(root=build_tree_node([5, 3, 6, 2, 4, null, 7]), key=3)
    assert Solution().deleteNode(root=build_tree_node([5, 3, 6, 2, 4, null, 7]), key=0)


if __name__ == '__main__':
    test()
