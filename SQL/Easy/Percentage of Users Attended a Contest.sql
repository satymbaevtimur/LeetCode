SELECT register.contest_id, ROUND(COUNT(DISTINCT register.user_id) * 100 / (SELECT COUNT(users.user_id) FROM users), 2) AS percentage 
FROM register 
GROUP BY register.contest_id 
ORDER BY percentage DESC, register.contest_id
