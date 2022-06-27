#!/usr/bin/env python
"""
CREATED AT: 2021/11/6
Des:

https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: BST

See: 
"""
from tree_node import TreeNode, build_tree_node


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Runtime: 105 ms, faster than 27.86%
        Memory Usage: 18.2 MB, less than 46.25%
        The number of nodes in the tree is in the range [2, 10^5].
        -10^9 <= Node.val <= 10^9
        All Node.val are unique.
        p != q
        p and q will exist in the BST.
        :param root:
        :param p:
        :param q:
        :return:
        """
        if p is None or q is None or root is None:
            raise ValueError('Value Error')
        if p.val > q.val:
            big, small = p.val, q.val
        else:
            big, small = q.val, p.val
        if small <= root.val <= big:
            return root
        if big < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)


def test():
    null = None
    tree = build_tree_node([6, 2, 8, 0, 4, 7, 9, null, null, 3, 5])
    assert Solution().lowestCommonAncestor(
        root=tree,
        p=TreeNode(2),
        q=TreeNode(8)) == tree
    assert Solution().lowestCommonAncestor(
        root=tree,
        p=TreeNode(2),
        q=TreeNode(4)) == build_tree_node([2, 0, 4, null, null, 3, 5])
    assert Solution().lowestCommonAncestor(
        root=build_tree_node([2, 1]),
        p=TreeNode(2),
        q=TreeNode(1)) == build_tree_node([2, 1])


if __name__ == '__main__':
    test()
