#!/usr/bin/env python3
"""
CREATED AT: 2022-09-08

URL: https://leetcode.com/problems/subtree-of-another-tree/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 572-SubtreeOfAnotherTree

Difficulty: Easy

Desc: 

Tag: 

See: 

"""
from tool import *
from tree_node import TreeNode


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Runtime: 284 ms, faster than 9.63%
        Memory Usage: 14.5 MB, less than 94.62%

        The number of nodes in the root tree is in the range [1, 2000].
        The number of nodes in the subRoot tree is in the range [1, 1000].
        -10^4 <= root.val <= 10^4
        -10^4 <= subRoot.val <= 10^4
        """

        def same(tree1, tree2) -> bool:
            if not tree1 and not tree2:
                return True
            if tree1 and tree2 and tree1.val == tree2.val:
                return same(tree1.left, tree2.left) and same(tree1.right, tree2.right)
            return False

        stack = [root]
        while stack:
            node = stack.pop()
            if node.val == subRoot.val and same(node, subRoot):
                return True
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False


def test():
    assert Solution().isSubtree(root=TreeNode.from_list([3, 4, 5, 1, 2]), subRoot=TreeNode.from_list([4, 1, 2]))
    assert not Solution().isSubtree(root=TreeNode.from_list([3, 4, 5, 1, 2, null, null, null, null, 0]),
                                    subRoot=TreeNode.from_list([4, 1, 2]))


if __name__ == '__main__':
    test()
