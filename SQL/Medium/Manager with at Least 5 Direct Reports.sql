SELECT e.name
FROM employee AS e
INNER JOIN employee AS t ON e.id = t.managerId
GROUP BY t.managerId
HAVING COUNT(t.managerId) >= 5
