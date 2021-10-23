# CREATED AT: 2021/9/19
# Des:
# https://leetcode.com/problems/combine-two-tables/
# GITHUB: https://github.com/Jiezhi/myleetcode
#
# Difficulty: Easy

# 7 / 7 test cases passed.
# Status: Accepted
# Runtime: 349 ms
# Memory Usage: 0B

# Write your MySQL query statement below
SELECT FirstName, LastName, City, State
FROM Person p
         LEFT JOIN
     Address a
     ON p.PersonId = a.PersonId;
