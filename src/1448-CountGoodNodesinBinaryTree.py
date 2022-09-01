#!/usr/bin/env python3
"""
CREATED AT: 2022-09-01

URL: https://leetcode.com/problems/count-good-nodes-in-binary-tree/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1448-CountGoodNodesInBinaryTree

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from tool import *
from tree_node import TreeNode


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        Runtime: 330 ms, faster than 72.00%
        Memory Usage: 32.7 MB, less than 7.60%

        The number of nodes in the binary tree is in the range [1, 10^5].
        Each node's value is between [-10^4, 10^4].
        """
        ret = 0
        stack = [(root, root.val)]
        while stack:
            node, val = stack.pop()
            if node.val >= val:
                ret += 1
            if node.left:
                stack.append((node.left, max(val, node.val)))
            if node.right:
                stack.append((node.right, max(val, node.val)))
        return ret

    def goodNodes2(self, root: TreeNode) -> int:
        """
        2021/8/17
        63 / 63 test cases passed.
        Status: Accepted
        Runtime: 244 ms
        Memory Usage: 31.5 MB
        :param root:
        :return:
        """
        good_nodes = 1
        dq = collections.deque()
        dq.append(root)
        while len(dq) > 0:
            node = dq.pop()
            if node.left:
                if node.val <= node.left.val:
                    good_nodes += 1
                else:
                    node.left.val = node.val
                dq.append(node.left)
            if node.right:
                if node.val <= node.right.val:
                    good_nodes += 1
                else:
                    node.right.val = node.val
                dq.append(node.right)

        return good_nodes


def test():
    assert Solution().goodNodes2(root=TreeNode.from_list([3, 1, 4, 3, null, 1, 5])) == 4
    assert Solution().goodNodes2(root=TreeNode.from_list([3, 3, null, 4, 2])) == 3
    assert Solution().goodNodes2(root=TreeNode.from_list([1])) == 1
    assert Solution().goodNodes(root=TreeNode.from_list([3, 1, 4, 3, null, 1, 5])) == 4
    assert Solution().goodNodes(root=TreeNode.from_list([3, 3, null, 4, 2])) == 3
    assert Solution().goodNodes(root=TreeNode.from_list([1])) == 1


if __name__ == '__main__':
    test()
