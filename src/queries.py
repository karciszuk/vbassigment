class SQL_Queries:
    class Portfolio:
        @staticmethod
        def users_aggregated():
            return """
            SELECT
                strftime('%Y-%m', registration_date) AS month,
                COUNT(DISTINCT user_id) AS new_users_count,
                CAST(AVG(age) AS INTEGER) AS avg_age,
                CAST(AVG(income) AS INTEGER) AS avg_income,
                CAST(AVG(credit_score) AS INTEGER) AS avg_credit_score
            FROM users
            WHERE registration_date > (
                SELECT date(MAX(registration_date), '-11 months') 
                FROM users
            )
            GROUP BY month 
            ORDER BY month
            """

        @staticmethod
        def transactions_aggregated():
            return """
            SELECT
                strftime('%Y-%m', transaction_date) AS month,
                COUNT(DISTINCT user_id) AS active_users_count,
                IFNULL(COUNT(transaction_id),0) AS transactions_count,
                SUM(transaction_amount) AS sum_amount,
                CAST(AVG(installments_count) AS INTEGER) AS avg_installments_count
            FROM transactions
            WHERE transaction_date > (
                SELECT date(MAX(transaction_date), '-11 months') 
                FROM transactions
            )
            GROUP BY month 
            ORDER BY month
            """

        @staticmethod
        def installment_plans():
            return """
            SELECT 
                strftime('%Y-%m', transaction_date) AS month, 
                SUM(CASE WHEN installments_count = 4 THEN transaction_amount ELSE 0 END) AS "4_installment_transaction_volume",
                SUM(CASE WHEN installments_count = 6 THEN transaction_amount ELSE 0 END) AS "6_installment_transaction_volume", 
                SUM(CASE WHEN installments_count = 12 THEN transaction_amount ELSE 0 END) AS "12_installment_transaction_volume",
                SUM(CASE WHEN installments_count = 24 THEN transaction_amount ELSE 0 END) AS "24_installment_transaction_volume"
            FROM transactions 
            WHERE transaction_date > (
                SELECT date(MAX(transaction_date), '-11 months') 
                FROM transactions
            )
            GROUP BY month
            ORDER BY month
            """

        @staticmethod
        def popular_categories():
            return """
            SELECT
                strftime('%Y-%m', transactions.transaction_date) AS month,
                merchants.category,
                COUNT(DISTINCT transactions.transaction_id) as category_transaction_count
            FROM merchants
            JOIN transactions ON merchants.merchant_id = transactions.merchant_id
            WHERE transaction_date > (
                SELECT date(MAX(transaction_date), '-11 months') 
                FROM transactions
            )
            GROUP BY month
            ORDER BY month
            """

    class DPD:
        @staticmethod
        def transactions():
            return """
            SELECT 
                transaction_id,
                user_id,
                transaction_date
            FROM transactions 
            """

        @staticmethod
        def installments():
            return """
            SELECT 
                transaction_id,
                installment_number,
                payment_date,
                scheduled_date
            FROM installments
            """

        @staticmethod
        def transactions_with_age_income():
            return """
            SELECT 
                transactions.transaction_id,
                transactions.user_id,
                users.age,
                users.income
            FROM transactions
            JOIN users ON transactions.user_id = users.user_id
            """
