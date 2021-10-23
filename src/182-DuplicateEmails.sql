# CREATED AT: 2021/9/19
# Des:
# https://leetcode.com/problems/duplicate-emails/
# GITHUB: https://github.com/Jiezhi/myleetcode
#
# Difficulty: Easy


# Write your MySQL query statement below


# 15 / 15 test cases passed.
# Status: Accepted
# Runtime: 367 ms
# Memory Usage: 0B

SELECT Email
FROM Person
GROUP BY Email
HAVING COUNT(Email) > 1;