#!/usr/bin/env python
"""
CREATED AT: 2021/8/4
Des:
https://leetcode.com/problems/path-sum-ii/
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge-2021/613/week-1-august-1st-august-7th/3838/
GITHUB: https://github.com/Jiezhi/myleetcode

"""
import collections
from typing import List

from tree_node import TreeNode, build_tree_node

null = None


class Solution:
    def pathSum2(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        """
        Updated at 2021/4/8
        Runtime: 41 ms, faster than 94.87%
        Memory Usage: 15.3 MB, less than 93.46%

        The number of nodes in the tree is in the range [0, 5000].
        -1000 <= Node.val <= 1000
        -1000 <= targetSum <= 1000
        """
        if not root:
            return []
        dq = collections.deque([(root, [root.val])])
        ret = []
        while dq:
            node, lst = dq.popleft()
            if not node.left and not node.right:
                if node.val == targetSum:
                    ret.append(lst)
            if node.left:
                tmp_value, node.left.val = node.left.val, node.left.val + node.val
                dq.append((node.left, lst + [tmp_value]))
            if node.right:
                tmp_value, node.right.val = node.right.val, node.right.val + node.val
                dq.append((node.right, lst + [tmp_value]))
        return ret

    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        """
        115 / 115 test cases passed.
        Status: Accepted
        Runtime: 44 ms
        Memory Usage: 20.4 MB
        :param root:
        :param targetSum:
        :return:
        """
        if root is None:
            return []
        paths = []

        def get_path_list(node: TreeNode, p_list: List[int]):
            if node is not None and node.val is not None:
                p_list.append(node.val)
            if not node.left and not node.right:
                paths.append(p_list)
            if node.left:
                get_path_list(node.left, p_list.copy())
            if node.right:
                get_path_list(node.right, p_list.copy())

        p_list = []
        # Get all paths
        get_path_list(root, p_list)
        ret = []
        for path in paths:
            if sum(path) == targetSum:
                ret.append(path)
        return ret


def test():
    assert Solution().pathSum(build_tree_node([0, 1, 1]), 1) == [[0, 1], [0, 1]]
    root1 = build_tree_node([5, 4, 8, 11, null, 13, 4, 7, 2, null, null, 5, 1])
    answer = [[5, 4, 11, 2], [5, 8, 4, 5]]
    ret = Solution().pathSum(root1, 22)
    assert len(answer) == len(ret)
    for r in ret:
        assert r in answer

    assert Solution().pathSum(build_tree_node([1, 2, 3]), 5) == []
    assert Solution().pathSum(build_tree_node([1, 2]), 0) == []
    assert Solution().pathSum(build_tree_node([]), 1) == []


if __name__ == '__main__':
    test()
