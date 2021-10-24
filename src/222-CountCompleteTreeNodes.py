#!/usr/bin/env python
"""
CREATED AT: 2021/10/24
Des:

https://leetcode.com/problems/count-complete-tree-nodes/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 
"""
import collections
from typing import Optional

from tree_node import TreeNode, build_tree_node


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        """
        The number of nodes in the tree is in the range [0, 5 * 10**4].
        0 <= Node.val <= 5 * 10**4
        The tree is guaranteed to be complete.
        :param root:
        :return:
        """
        if root is None:
            return 0
        dq = collections.deque()
        dq.append(root)
        ret = 0
        while len(dq) > 0:
            node = dq.pop()
            ret += 1
            if node.left is not None:
                dq.append(node.left)
            if node.right is not None:
                dq.append(node.right)
        return ret

    def countNodes2(self, root: Optional[TreeNode]) -> int:
        """
        Runtime: 90 ms, faster than 49.51%
        Memory Usage: 21.6 MB, less than 57.82%
        Reference: https://leetcode.com/problems/count-complete-tree-nodes/discuss/62088/My-python-solution-in-O(lgn-*-lgn)-time
        The number of nodes in the tree is in the range [0, 5 * 10**4].
        0 <= Node.val <= 5 * 10**4
        The tree is guaranteed to be complete.
        :param root:
        :return:
        """

        def get_tree_height(tree):
            if tree is None:
                return 0
            return 1 + get_tree_height(tree.left)

        if root is None:
            return 0

        left_height = get_tree_height(root.left)
        right_height = get_tree_height(root.right)
        if left_height == right_height:
            # left sub tree must be a full binary tree
            return 2 ** left_height + self.countNodes(root.right)
        else:
            # right sub tree must be a full binary tree
            return 2 ** right_height + self.countNodes(root.left)


def test():
    assert Solution().countNodes2(root=build_tree_node([])) == 0
    assert Solution().countNodes2(root=build_tree_node([1])) == 1
    assert Solution().countNodes2(root=build_tree_node([1, 2])) == 2
    assert Solution().countNodes2(root=build_tree_node([1, 2, 3])) == 3
    assert Solution().countNodes2(root=build_tree_node([1, 2, 3, 4])) == 4
    assert Solution().countNodes2(root=build_tree_node([1, 2, 3, 4, 5])) == 5
    assert Solution().countNodes2(root=build_tree_node([1, 2, 3, 4, 5, 6])) == 6


if __name__ == '__main__':
    test()
