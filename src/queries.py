class SQL_Queries:
    class Portfolio:
        @staticmethod
        def new_customers():
            return """
            SELECT
                strftime('%Y-%m', registration_date) AS month,
                COUNT(DISTINCT user_id) AS new_user_count
            FROM users 
            WHERE registration_date > (
                SELECT date(MAX(registration_date), '-11 months') 
                FROM users
            )
            GROUP BY month 
            ORDER BY month
            """

        @staticmethod
        def active_customers():
            return """
            SELECT
                strftime('%Y-%m', users.registration_date) AS month,
                COUNT(DISTINCT users.user_id) AS active_user_count
            FROM users
            JOIN transactions ON users.user_id = transactions.user_id
             WHERE registration_date > (
                SELECT date(MAX(registration_date), '-11 months') 
                FROM users
            )
            GROUP BY month 
            ORDER BY month
            """

        @staticmethod
        def transaction_volume():
            return """
            SELECT 
                strftime('%Y-%m', transaction_date) AS month,
                COUNT(DISTINCT transaction_id) AS transaction_count,
                SUM(transaction_amount) as transaction_amount
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

    class Payment:
        @staticmethod
        def define_dpd_aggregate():
            return """
            SELECT 
                transaction_id,
                installment_number,
                payment_date,
                scheduled_date
            FROM installments
            """

        @staticmethod
        def define_dpd90_rate():
            return """
            """

        @staticmethod
        def calculate_dpd90_trend():
            return """
            SELECT 
                transactions.transaction_id,
                transactions.user_id,
                users.age,
                users.income
            FROM transactions
            JOIN users ON transactions.user_id = users.user_id
            """

    class Vintage:
        @staticmethod
        def q1():
            return """
            SELECT 
                transaction_id,
                user_id,
                transaction_date
            FROM transactions 
            """

        @staticmethod
        def q2():
            return """
            SELECT 
                transaction_id,
                installment_number,
                payment_date,
                scheduled_date
            FROM installments
            """
