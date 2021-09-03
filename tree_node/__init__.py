#!/usr/bin/env python
"""
Github: https://github.com/Jiezhi/myleetcode

Created on 2019-03-18

Leetcode: https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/928/
"""

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other):
        if self is None and other is None:
            return True
        if self is None or other is None:
            return False
        if self.val != other.val:
            return False
        while self is not None and other is not None:
            return self.left == other.left and self.right == other.right

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return str(get_tree_node_list(self))


def build_tree_node(nums) -> TreeNode:
    if not nums:
        return None
    num_nodes = []
    for num in nums:
        if num is not None:
            num_nodes.append(TreeNode(num))
        else:
            num_nodes.append(None)
    l = len(nums)
    i = 0
    nulls = 0
    while (i - nulls) <= (l / 2 - 1):
        if num_nodes[i]:
            num_nodes[i].left = num_nodes[2 * (i - nulls) + 1]
            if 2 * (i - nulls) + 2 < l:
                num_nodes[i].right = num_nodes[2 * (i - nulls) + 2]
        else:
            nulls += 1
        i += 1
    return num_nodes[0]


def print_tree_node(tree_node: TreeNode):
    if tree_node and tree_node.val is not None:
        print(tree_node.val)
        print_tree_node(tree_node.left)
        print_tree_node(tree_node.right)


def get_tree_node_list(tree_node: TreeNode) -> List[int]:
    ret = []
    if tree_node and tree_node.val is not None:
        ret.append(tree_node.val)
        ret.append(get_tree_node_list(tree_node.left))
        ret.append(get_tree_node_list(tree_node.right))
    return ret if len(ret) > 0 else None


if __name__ == '__main__':
    tree = build_tree_node([1, None, 2, None, 3, 4, 5, 6, None, 8])
    print_tree_node(tree)

    tree = build_tree_node([0, 1, 1])
    print_tree_node(tree)

    print(get_tree_node_list(tree))

    assert build_tree_node([1, 2, 3, None, None, 4, 5]) == build_tree_node([1, 2, 3, None, None, 4, 5])
