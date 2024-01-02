SELECT prices.product_id, IFNULL(ROUND(SUM(units * price) / SUM(units), 2), 0) AS average_price
FROM prices 
LEFT JOIN unitssold ON prices.product_id = unitssold.product_id 
AND unitssold.purchase_date BETWEEN start_date AND end_date
GROUP BY prices.product_id;
