class SQL_Queries:
    test =  "SELECT * FROM Users LIMIT 10;"

    monthly_users = "SELECT COUNT(user_id) AS user_count, strftime('%m', registration_date) AS month FROM Users GROUP BY month ORDER BY month"