SELECT signups.user_id, ROUND(AVG(IF(confirmations.action = "confirmed", 1, 0)), 2) AS confirmation_rate
FROM signups 
LEFT JOIN Confirmations ON signups.user_id = confirmations.user_id 
GROUP BY user_id;
