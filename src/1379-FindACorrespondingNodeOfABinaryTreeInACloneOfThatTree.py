#!/usr/bin/env python
"""
CREATED AT: 2022/5/17
Des:
https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""
import collections
from tree_node import TreeNode


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        """
        Runtime: 973 ms, faster than 21.38%
        Memory Usage: 24 MB, less than 68.23%
        The number of nodes in the tree is in the range [1, 10^4].
        The values of the nodes of the tree are unique.
        target node is a node from the original tree and is not null.
        :param original:
        :param cloned:
        :param target:
        :return:
        """
        val = target.val
        dq = collections.deque([cloned])
        while dq:
            node = dq.popleft()
            if node.val == val:
                return node
            if node.left:
                dq.append(node.left)
            if node.right:
                dq.append(node.right)


def test():
    # No Test here.
    pass


if __name__ == '__main__':
    test()
