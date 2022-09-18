#!/usr/bin/env python3
"""
CREATED AT: 2022-09-18

URL: https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 2415-ReverseOddLevelsOfBinaryTree

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from tool import *
from tree_node import TreeNode


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def reverse(node_list):
            i, j = 0, len(node_list) - 1
            while i < j:
                node_list[i].val, node_list[j].val = node_list[j].val, node_list[i].val
                i += 1
                j -= 1

        dq = collections.deque([(root, 0)])
        node_list = []
        while dq:
            node, level = dq.popleft()
            if not node:
                break
            if level & 1 == 1:
                node_list.append(node)
            else:
                # reach the even level, reverse pre level
                reverse(node_list)
                node_list.clear()
                pass
            dq.append((node.left, level + 1))
            dq.append((node.right, level + 1))
        if node_list:
            reverse(node_list)

        return root


def test():
    assert Solution().reverseOddLevels(root=TreeNode.from_list([2, 3, 5, 8, 13, 21, 34])) == TreeNode.from_list(
        [2, 5, 3, 8, 13, 21, 34])
    assert Solution().reverseOddLevels(
        root=TreeNode.from_list([0, 1, 2, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2])) == TreeNode.from_list(
        [0, 2, 1, 0, 0, 0, 0, 2, 2, 2, 2, 1, 1, 1, 1])


if __name__ == '__main__':
    test()
