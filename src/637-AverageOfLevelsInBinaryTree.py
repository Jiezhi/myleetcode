#!/usr/bin/env python3
"""
CREATED AT: 2022-09-02

URL: https://leetcode.com/problems/average-of-levels-in-binary-tree/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 637-AverageOfLevelsInBinaryTree

Difficulty: Easy

Desc: 

Tag: 

See: 

"""
from tool import *
from tree_node import TreeNode


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        """
        Runtime: 97 ms, faster than 22.67%
        Memory Usage: 16.5 MB, less than 87.46%

        The number of nodes in the tree is in the range [1, 10^4].
        -2^31 <= Node.val <= 2^31 - 1
        """
        ret = []
        dq = collections.deque([(root, 1)])
        pre, size, total = 1, 0, 0
        while dq:
            node, level = dq.popleft()
            if level != pre:
                ret.append(total / size)
                pre, size, total = level, 1, node.val
            else:
                size += 1
                total += node.val
            if node.left:
                dq.append((node.left, level + 1))
            if node.right:
                dq.append((node.right, level + 1))
        ret.append(total / size)
        return ret


def test():
    assert Solution().averageOfLevels(root=TreeNode.from_list([1])) == [1]
    assert Solution().averageOfLevels(root=TreeNode.from_list([3, 9, 20, null, null, 15, 7])) == [3.00000, 14.50000,
                                                                                                  11.00000]
    assert Solution().averageOfLevels(root=TreeNode.from_list([3, 9, 20, 15, 7])) == [3.00000, 14.50000, 11.00000]


if __name__ == '__main__':
    test()
