#!/usr/bin/env python
"""
Github: https://github.com/Jiezhi/myleetcode

Created on 2019-03-18

Leetcode: https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/928/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


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


if __name__ == '__main__':
    tree = build_tree_node([1, None, 2, None, 3, 4, 5, 6, None, 8])
    print_tree_node(tree)

    tree = build_tree_node([0, 1, 1])
    print_tree_node(tree)
