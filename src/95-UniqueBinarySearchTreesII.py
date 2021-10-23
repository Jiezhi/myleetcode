#!/usr/bin/env python
"""
CREATED AT: 2021/9/2
Des:
https://leetcode.com/problems/unique-binary-search-trees-ii/
https://leetcode.com/explore/item/3961
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: 1

"""
import itertools
from typing import List, Optional

from tool import print_results
from tree_node import TreeNode, get_tree_node_list


class Solution:
    @print_results
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        """
        8 / 8 test cases passed.
        Status: Accepted
        Runtime: 92 ms
        Memory Usage: 15.7 MB
        :param n:
        :return:
        """

        def dp(nums: List[int]) -> List[Optional[TreeNode]]:
            if len(nums) == 0:
                return [None]
            if len(nums) == 1:
                return [TreeNode(nums[0])]
            ret = []
            for i in range(len(nums)):
                left_list = dp(nums[:i])
                right_list = dp(nums[i + 1:])
                for left, right in itertools.product(left_list, right_list):
                    root = TreeNode(nums[i])
                    root.left = left
                    root.right = right
                    ret.append(root)

            return ret

        return dp(list(range(1, n + 1)))


def test():
    null = None
    ans = [[1, null, 2, null, 3], [1, null, 3, 2], [2, 1, 3], [3, 1, null, null, 2], [3, 2, null, 1]]
    # assert Solution().generateTrees(n=1)
    ret = Solution().generateTrees(n=3)
    # print(ret)
    ret = Solution().generateTrees(n=8)


if __name__ == '__main__':
    test()
