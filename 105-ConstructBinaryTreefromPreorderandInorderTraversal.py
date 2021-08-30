#!/usr/bin/env python
"""
CREATED AT: 2021/8/29
Des:
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/788/
GITHUB: https://github.com/Jiezhi/myleetcode

"""
from typing import List, Optional

import tree_node
from tree_node import TreeNode, build_tree_node


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        203 / 203 test cases passed.
        Status: Accepted
        Runtime: 240 ms
        Memory Usage: 88.3 MB
        :param preorder:
        :param inorder:
        :return:
        """
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root
        root_index = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:root_index + 1], inorder[:root_index])
        root.right = self.buildTree(preorder[root_index + 1:], inorder[root_index + 1:])
        return root


def test():
    null = None
    ans = build_tree_node([3, 9, 20, null, null, 15, 7])
    assert Solution().buildTree(preorder=[3, 9, 20, 15, 7], inorder=[9, 3, 15, 20, 7]) == ans

    ans = build_tree_node([-1])
    assert Solution().buildTree(preorder=[-1], inorder=[-1]) == ans

    ans = build_tree_node([1, null, 2])
    assert Solution().buildTree(preorder=[1, 2], inorder=[1, 2]) == ans

    ans = build_tree_node([1, 2])
    assert Solution().buildTree(preorder=[1, 2], inorder=[2, 1]) == ans


if __name__ == '__main__':
    test()
