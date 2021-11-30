#!/usr/bin/env python
"""
Des:
CREATED AT: 2021/11/30
Des:

https://leetcode.com/problems/linked-list-cycle-ii/
https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1214/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag:

See:

Reference: https://leetcode.com/problems/linked-list-cycle-ii/discuss/44783/Share-my-python-solution-with-detailed-explanation/44321
"""

from list_node import ListNode, buildCycleList


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        """
        16 / 16 test cases passed.
        Status: Accepted
        Runtime: 52 ms
        Memory Usage: 17.2 MB
        The number of the nodes in the list is in the range [0, 10^4].
        -10^5 <= Node.val <= 10^5
        pos is -1 or a valid index in the linked-list.
        :param head:
        :return:
        """
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                slow2 = head
                while slow != slow2:
                    slow = slow.next
                    slow2 = slow2.next
                return slow


def test():
    # ret = Solution().detectCycle(buildCycleList(nums=[3, 2, 0, -4], pos=1))
    # assert ret.val == 2
    #
    # ret = Solution().detectCycle(buildCycleList(nums=[1, 2], pos=0))
    # assert ret.val == 0
    pass


if __name__ == '__main__':
    test()
