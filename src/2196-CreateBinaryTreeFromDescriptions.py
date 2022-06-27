#!/usr/bin/env python
"""
CREATED AT: 2022/3/6
Des:

https://leetcode.com/problems/create-binary-tree-from-descriptions/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

Time Spent:  min
"""
import collections
from typing import List, Optional

from tree_node import TreeNode, build_tree_node


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        """
        1 <= descriptions.length <= 104
        descriptions[i].length == 3
        1 <= parenti, childi <= 105
        0 <= isLefti <= 1
        The binary tree described by descriptions is valid.
        """
        nodes = collections.defaultdict(list)
        p_nodes = collections.defaultdict(int)
        for p, c, l in descriptions:
            nodes[p].append((c, l))
            p_nodes[c] = p
        # get the root node
        root = TreeNode([x for x in nodes.keys() if not p_nodes[x]][0])

        dq = collections.deque([root])
        while dq:
            node = dq.pop()
            for child in nodes[node.val]:
                if child[1] == 1:
                    node.left = TreeNode(child[0])
                    dq.append(node.left)
                else:
                    node.right = TreeNode(child[0])
                    dq.append(node.right)
        return root


def test():
    assert Solution().createBinaryTree(
        descriptions=[[20, 15, 1], [20, 17, 0], [50, 20, 1], [50, 80, 0], [80, 19, 1]]) == build_tree_node(
        [50, 20, 80, 15, 17, 19])


if __name__ == '__main__':
    test()
