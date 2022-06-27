#!/usr/bin/env python
"""
CREATED AT: 2021/11/21
Des:

GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: Tree

See: 
"""
from typing import List, Optional

from tree_node import TreeNode, build_tree_node


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        """
        Runtime: 188 ms, faster than 34.23%
        Memory Usage: 88.6 MB, less than 16.53%

        1 <= inorder.length <= 3000
        postorder.length == inorder.length
        -3000 <= inorder[i], postorder[i] <= 3000
        inorder and postorder consist of unique values.
        Each value of postorder also appears in inorder.
        inorder is guaranteed to be the inorder traversal of the tree.
        postorder is guaranteed to be the postorder traversal of the tree.
        :param inorder:
        :param postorder:
        :return:
        """
        if not inorder:
            return None
        root = TreeNode(postorder[-1])
        root_index = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:root_index], postorder[:root_index])
        root.right = self.buildTree(inorder[root_index + 1:], postorder[root_index: -1])
        return root


def test():
    null = None
    assert Solution().buildTree(inorder=[9, 3, 15, 20, 7], postorder=[9, 15, 7, 20, 3]) == \
           build_tree_node([3, 9, 20, null, null, 15, 7])

    assert Solution().buildTree(inorder=[-1], postorder=[-1]) == build_tree_node([-1])
    assert Solution().buildTree(inorder=[2, 1, 3], postorder=[2, 3, 1]) == build_tree_node([1, 2, 3])
    assert Solution().buildTree(inorder=[2, 1], postorder=[2, 1]) == build_tree_node([1, 2])
    assert Solution().buildTree(inorder=[1, 3], postorder=[3, 1]) == build_tree_node([1, null, 3])


if __name__ == '__main__':
    test()
