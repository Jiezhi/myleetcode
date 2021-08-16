#!/usr/bin/env python
"""
CREATED AT: 2021/8/16
Des:

https://leetcode.com/problems/palindrome-linked-list/
https://leetcode.com/explore/featured/card/top-interview-questions-easy/93/linked-list/772/
GITHUB: https://github.com/Jiezhi/myleetcode

"""

from typing import Optional

import list_node
from list_node import ListNode


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
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


def test():
    assert Solution().isPalindrome(list_node.buildListNode([1, 2, 2, 1]))
    assert Solution().isPalindrome(list_node.buildListNode([1]))
    assert not Solution().isPalindrome(list_node.buildListNode([1, 2]))
    assert Solution().isPalindrome(list_node.buildListNode([1, 1]))


if __name__ == '__main__':
    test()
