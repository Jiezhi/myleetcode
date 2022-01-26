#!/usr/bin/env python
"""
CREATED AT: 2022/1/26
Des:

https://leetcode.com/problems/all-elements-in-two-binary-search-trees/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

Time Spent:  min
"""
from typing import List

from src.tree_node import TreeNode, build_tree_node


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        """
        CREATED AT: 2022/1/26
        Runtime: 332 ms, faster than 81.69%
        Memory Usage: 22.7 MB, less than 21.43%
        The number of nodes in each tree is in the range [0, 5000].
        -10^5 <= Node.val <= 10^5
        :param root1:
        :param root2:
        :return:
        """

        dq1, dq2 = [], []

        def mid_dfs(node, dq):
            if node.left:
                mid_dfs(node.left, dq)
            dq.append(node.val)
            if node.right:
                mid_dfs(node.right, dq)

        if root1:
            mid_dfs(root1, dq1)
        if root2:
            mid_dfs(root2, dq2)

        ret = []
        i, j = 0, 0
        while i < len(dq1) and j < len(dq2):
            if dq1[i] < dq2[j]:
                ret.append(dq1[i])
                i += 1
            else:
                ret.append(dq2[j])
                j += 1
        for k in range(i, len(dq1)):
            ret.append(dq1[k])
        for k in range(j, len(dq2)):
            ret.append(dq2[k])

        return ret


def test():
    root1 = build_tree_node([2, 1, 4])
    root2 = build_tree_node([])
    assert Solution().getAllElements(root1, root2) == [1, 2, 4]

    root1 = build_tree_node([2, 1, 4])
    root2 = build_tree_node([1, 0, 3])
    assert Solution().getAllElements(root1, root2) == [0, 1, 1, 2, 3, 4]

    root1 = build_tree_node([1, None, 8])
    root2 = build_tree_node([8, 1])
    assert Solution().getAllElements(root1, root2) == [1, 1, 8, 8]


if __name__ == '__main__':
    test()
