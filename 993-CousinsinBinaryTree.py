#!/usr/bin/env python
"""
CREATED AT: 2021/10/18
Des:

https://leetcode.com/problems/cousins-in-binary-tree/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: Tree

See: 
"""

from typing import Optional

from tree_node import TreeNode, build_tree_node


class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        """
        Runtime: 28 ms, faster than 93.30%
        Memory Usage: 14.3 MB, less than 71.37%

        The number of nodes in the tree is in the range [2, 100].
        1 <= Node.val <= 100
        Each node has a unique value.
        x != y
        x and y are exist in the tree.
        :param root:
        :param x:
        :param y:
        :return:
        """
        if root.val == x or root.val == y:
            return False
        parent_list = [root]
        cur_list = []
        while len(parent_list) > 0:
            cur_val_list = []
            for node in parent_list:
                if node.left is not None and node.right is not None:
                    if node.left.val in [x, y] and node.right.val in [x, y]:
                        return False
                if node.left is not None:
                    cur_list.append(node.left)
                    cur_val_list.append(node.left.val)
                if node.right is not None:
                    cur_list.append(node.right)
                    cur_val_list.append(node.right.val)
            if x in cur_val_list:
                if y in cur_val_list:
                    return True
                else:
                    return False
            if y in cur_val_list:
                return False
            parent_list = cur_list.copy()
            cur_list = []
        return False


def test():
    null = None
    assert not Solution().isCousins(root=build_tree_node([1, 2, 3, null, 4]), x=2, y=3)
    assert not Solution().isCousins(root=build_tree_node([1, 2, 3, 4]), x=4, y=3)
    assert Solution().isCousins(root=build_tree_node([1, 2, 3, null, 4, null, 5]), x=5, y=4)


if __name__ == '__main__':
    test()
