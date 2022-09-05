#!/usr/bin/env python3
"""
CREATED AT: 2022-09-05

URL: https://leetcode.com/problems/find-duplicate-subtrees/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 652-FindDuplicateSubtrees

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from tool import *
from tree_node import TreeNode


class Solution:
    @print_results
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        """
        LTE on leetcode.com, but passed on leetcode.cn
        执行用时：3748 ms, 在所有 Python3 提交中击败了5.01%的用户
        内存消耗：263.1 MB, 在所有 Python3 提交中击败了5.01%的用户
        通过测试用例：176 / 176

        The number of the nodes in the tree will be in the range [1, 10^4]
        -200 <= Node.val <= 200
        """

        @cache
        def equal(node1, node2) -> bool:
            if not node1 and not node2:
                return True
            if node1 and node2 and node1.val == node2.val:
                return equal(node1.left, node2.left) and equal(node1.right, node2.right)
            return False

        ret = []
        memo = collections.defaultdict(list)

        stack = [root]
        while stack:
            node = stack.pop()
            if memo[node.val]:
                found = False
                for i in range(len(memo[node.val])):
                    if equal(node, memo[node.val][i][0]):
                        found = True
                        if not memo[node.val][i][1]:
                            ret.append(node)
                            memo[node.val][i] = (memo[node.val][i][0], True)
                        break
                if not found:
                    memo[node.val].append((node, False))
            else:
                memo[node.val].append((node, False))
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return ret


def test():
    # FIXME: add hash function to TreeNode
    pass
    # assert Solution().findDuplicateSubtrees(root=TreeNode.from_list([1, 2, 3, 4, null, 2, 4, null, null, 4])) in [
    #     TreeNode.from_list([4]), TreeNode.from_list([2, 4])]
    # assert Solution().findDuplicateSubtrees(root=TreeNode.from_list([2, 1, 1])) == [TreeNode.from_list([1])]
    # assert Solution().findDuplicateSubtrees(root=TreeNode.from_list([2, 2, 2, 3, null, 3, null])) == [
    #     TreeNode.from_list([2, 3]), TreeNode.from_list([3])]


if __name__ == '__main__':
    test()
