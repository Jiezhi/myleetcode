#!/usr/bin/env python
"""
CREATED AT: 2021/8/29
Des:
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/787/
GITHUB: https://github.com/Jiezhi/myleetcode

"""
from typing import Optional, List

from tree_node import TreeNode, build_tree_node


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        33 / 33 test cases passed.
        Status: Accepted
        Runtime: 28 ms
        Memory Usage: 14.6 MB
        :param root:
        :return:
        """
        if root is None:
            return []
        ret = []
        current_level = [root]
        left_to_right = -1
        while len(current_level) > 0:
            tmp_list = []
            next_level = []
            for node in current_level:
                tmp_list.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            current_level = next_level.copy()
            if left_to_right == 1:
                tmp_list.reverse()
            ret.append(tmp_list)
            left_to_right *= -1
        return ret


def test():
    null = None
    assert Solution().zigzagLevelOrder(build_tree_node([1, 2, 3, 4, null, null, 5])) == [[1], [3, 2], [4, 5]]
    assert Solution().zigzagLevelOrder(build_tree_node([3, 9, 20, null, null, 15, 7])) == [[3], [20, 9], [15, 7]]
    assert Solution().zigzagLevelOrder(build_tree_node([1])) == [[1]]
    assert Solution().zigzagLevelOrder(build_tree_node([])) == []


if __name__ == '__main__':
    test()
