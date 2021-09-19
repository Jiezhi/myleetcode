# CREATED AT: 2021/9/19
# Des:
# https://leetcode.com/problems/employees-earning-more-than-their-managers/
# GITHUB: https://github.com/Jiezhi/myleetcode
#
# Difficulty: Easy


# Write your MySQL query statement below

# 14 / 14 test cases passed.
# Status: Accepted
# Runtime: 348 ms
# Memory Usage: 0B

select e1.Name AS Employee
FROM Employee e1
         LEFT JOIN Employee e2
                   ON e1.ManagerId = e2.id
WHERE e1.Salary > e2.Salary;
