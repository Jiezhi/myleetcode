#!/usr/bin/env python
"""
CREATED AT: 2021/9/27
Des:

https://leetcode.com/problems/unique-email-addresses
https://leetcode.com/explore/item/3989
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy
"""
from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        """
        183 / 183 test cases passed.
        Status: Accepted
        Runtime: 48 ms
        Memory Usage: 14.3 MB
        :param emails:
        :return:
        """
        email_set = set()

        for email in emails:
            p_index = email.find('+')
            at_index = email.index('@')
            if p_index > -1:
                email_set.add(email[:p_index].replace('.', '') + email[at_index:])
            else:
                email_set.add(email[:at_index].replace('.', '') + email[at_index:])
        print(email_set)
        return len(email_set)


def test():
    assert Solution().numUniqueEmails(["test.email+alex@leetcode.com", "test.email@leetcode.com"]) == 1

    assert Solution().numUniqueEmails(
        emails=["test.email+alex@leetcode.com",
                "test.e.mail+bob.cathy@leetcode.com",
                "testemail+david@lee.tcode.com"]) == 2

    assert Solution().numUniqueEmails(emails=["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]) == 3


if __name__ == '__main__':
    test()
