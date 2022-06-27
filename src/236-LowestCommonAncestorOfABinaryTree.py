#!/usr/bin/env python
"""
CREATED AT: 2022/3/3
Des:
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

Time Spent:  min
"""

from typing import Optional, List

from tree_node import TreeNode, build_tree_node


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Runtime: 1479 ms, faster than 5.00%
        Memory Usage: 26.1 MB, less than 65.66%

        The number of nodes in the tree is in the range [2, 10^5].
        -10^9 <= Node.val <= 10^9
        All Node.val are unique.
        p != q
        p and q will exist in the tree.
        """

        def getNodePath(tree, target) -> Optional[List[TreeNode]]:
            if not tree:
                return None
            if tree.val == target.val:
                return [tree]
            if tree.left:
                ret = getNodePath(tree.left, target)
                if ret:
                    return [tree] + ret
            if tree.right:
                ret = getNodePath(tree.right, target)
                if ret:
                    return [tree] + ret
            return None

        # TODO: search p and q can be done in one search
        ppath = getNodePath(root, p)
        qpath = getNodePath(root, q)

        i = 0
        l = min(len(ppath), len(qpath))
        while i < l:
            if ppath[i] != qpath[i]:
                return ppath[i - 1]
            i += 1
        return ppath[l - 1]


def test():
    null = None
    assert Solution().lowestCommonAncestor(
        root=build_tree_node([3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]),
        p=build_tree_node([5]),
        q=build_tree_node([1])).val == build_tree_node([3]).val


if __name__ == '__main__':
    test()
