#!/usr/bin/env python3
"""
CREATED AT: 2022-08-23

URL: https://leetcode.com/problems/palindrome-linked-list/
https://leetcode.com/explore/featured/card/top-interview-questions-easy/93/linked-list/772/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 234-PalindromeLinkedList

Difficulty: Easy

Desc: 

Tag: 

See: 206

"""
from list_node import ListNode
from tool import *


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        2022-08-23
        Runtime: 947 ms, faster than 78.82%
        Memory Usage: 39 MB, less than 76.71%
        The number of nodes in the list is in the range [1, 10^5].
        0 <= Node.val <= 9
        """
        l = 0
        node = head
        while node:
            node = node.next
            l += 1

        def reverse(node):
            pre = None
            while node:
                pre, node.next, node = node, pre, node.next
            return pre

        i = l // 2
        node = head
        while i > 0:
            node = node.next
            i -= 1

        node = reverse(node)

        while node:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return True

    def isPalindrome2(self, head: Optional[ListNode]) -> bool:
        """
        2021/8/16
        85 / 85 test cases passed.
        Status: Accepted
        Runtime: 864 ms
        Memory Usage: 47.5 MB
        :param head:
        :return:
        """
        nums = [head.val]
        while head.next:
            nums.append(head.next.val)
            head = head.next
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i] != nums[j]:
                return False
            i += 1
            j -= 1
        return True


# def test():
#     func = [Solution().isPalindrome, Solution().isPalindrome2]
#     l1 = ListNode.from_list([1, 1, 2, 1])
#     params = [(l1, False),
#               (ListNode.from_list([1, 2, 3, 4, 3, 2, 1]), True)]
#     for p in itertools.product(func, params):
#         print(len(p), p)


def test():
    assert not Solution().isPalindrome2(head=ListNode.from_list([1, 1, 2, 1]))
    assert Solution().isPalindrome2(head=ListNode.from_list([1, 2, 3, 4, 3, 2, 1]))
    assert Solution().isPalindrome2(head=ListNode.from_list([1, 2, 3, 3, 2, 1]))
    assert Solution().isPalindrome2(head=ListNode.from_list([1, 2, 2, 1]))
    assert not Solution().isPalindrome2(head=ListNode.from_list([1, 2]))
    assert Solution().isPalindrome2(head=ListNode.from_list([1]))
    assert Solution().isPalindrome2(head=ListNode.from_list([1, 1]))

    assert not Solution().isPalindrome(head=ListNode.from_list([1, 1, 2, 1]))
    assert Solution().isPalindrome(head=ListNode.from_list([1, 2, 3, 4, 3, 2, 1]))
    assert Solution().isPalindrome(head=ListNode.from_list([1, 2, 3, 3, 2, 1]))
    assert Solution().isPalindrome(head=ListNode.from_list([1, 2, 2, 1]))
    assert not Solution().isPalindrome(head=ListNode.from_list([1, 2]))
    assert Solution().isPalindrome(head=ListNode.from_list([1]))
    assert Solution().isPalindrome(head=ListNode.from_list([1, 1]))


if __name__ == '__main__':
    test()
