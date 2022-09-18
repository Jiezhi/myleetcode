#!/usr/bin/env python3
"""
CREATED AT: 2022-09-18

URL: https://leetcode.com/problems/count-days-spent-together/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 2409-CountDaysSpentTogether

Difficulty: Easy

Desc: 

Tag: 

See: 

"""


class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        """
        All dates are provided in the format "MM-DD".
        Alice and Bob's arrival dates are earlier than or equal to their leaving dates.
        The given dates are valid dates of a non-leap year.
        """
        mon_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        alice_a, alice_l = arriveAlice.split('-'), leaveAlice.split('-')
        bob_a, bob_l = arriveBob.split('-'), leaveBob.split('-')
        alice_ad, alice_ld = sum(mon_days[:int(alice_a[0]) - 1]) + int(alice_a[1]), sum(
            mon_days[:int(alice_l[0]) - 1]) + int(alice_l[1])
        bob_ad, bob_ld = sum(mon_days[:int(bob_a[0]) - 1]) + int(bob_a[1]), sum(mon_days[:int(bob_l[0]) - 1]) + int(
            bob_l[1])
        if alice_ad <= bob_ad <= alice_ld <= bob_ld:
            return alice_ld - bob_ad + 1
        elif bob_ad <= alice_ad <= bob_ld <= alice_ld:
            return bob_ld - alice_ad + 1
        elif alice_ad <= bob_ad <= bob_ld <= alice_ld:
            return bob_ld - bob_ad + 1
        elif bob_ad <= alice_ad <= alice_ld <= bob_ld:
            return alice_ld - alice_ad + 1
        return 0


def test():
    assert Solution().countDaysTogether(arriveAlice="08-15", leaveAlice="08-18", arriveBob="08-16",
                                        leaveBob="08-19") == 3
    assert Solution().countDaysTogether(arriveAlice="10-01", leaveAlice="10-31", arriveBob="11-01",
                                        leaveBob="12-31") == 0


if __name__ == '__main__':
    test()
