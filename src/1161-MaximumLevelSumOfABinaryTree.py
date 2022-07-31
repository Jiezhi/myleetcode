#!/usr/bin/env python3
"""
CREATED AT: 2022-07-31

URL: https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1161-MaximumLevelSumOfABinaryTree

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from tool import *
from tree_node import TreeNode


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        """
        Runtime: 452 ms, faster than 52.36%
        Memory Usage: 18.8 MB, less than 30.91%

        The number of nodes in the tree is in the range [1, 10^4].
        -10^5 <= Node.val <= 10^5
        """
        ret = (1, -math.inf)
        pre, total = 1, 0
        dq = collections.deque([(root, 1)])
        while dq:
            node, pos = dq.popleft()
            if pos != pre:
                if total > ret[1]:
                    ret = (pos - 1, total)
                pre, total = pos, 0
            total += node.val
            if node.left:
                dq.append((node.left, pos + 1))
            if node.right:
                dq.append((node.right, pos + 1))
        if total > ret[1]:
            return pre
        return ret[0]


def test():
    assert Solution().maxLevelSum(root=TreeNode.from_list([-100, -200, -300, -20, -5, -10, null])) == 3
    assert Solution().maxLevelSum(root=TreeNode.from_list([1, 7, 0, 7, -8, null, null])) == 2
    assert Solution().maxLevelSum(
        root=TreeNode.from_list([989, null, 10250, 98693, -89388, null, null, null, -32127])) == 2


if __name__ == '__main__':
    test()
