SELECT activity.machine_id, ROUND(AVG(activity_new.timestamp - activity.timestamp), 3) AS processing_time
FROM activity
INNER JOIN activity activity_new ON activity_new.machine_id = activity.machine_id
WHERE activity.activity_type = 'start' AND activity_new.activity_type = 'end'
GROUP BY activity.machine_id
