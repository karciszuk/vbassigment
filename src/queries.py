class SQL_Queries:
    
    class Portfolio:
        @staticmethod
        def new_customers():
            return """
            SELECT
                strftime('%Y-%m', registration_date) AS month,
                COUNT(DISTINCT user_id) AS user_count
            FROM users 
            WHERE registration_date > (
                SELECT date(MAX(registration_date), '-12 months') 
                FROM users
            )
            GROUP BY month 
            ORDER BY month
            """
        
        @staticmethod
        def active_customers():
            return  """
            SELECT
                strftime('%Y-%m', users.registration_date) AS month,
                COUNT(DISTINCT users.user_id) AS user_count
            FROM users
            JOIN transactions ON users.user_id = transactions.user_id
             WHERE registration_date > (
                SELECT date(MAX(registration_date), '-12 months') 
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
                SELECT date(MAX(transaction_date), '-12 months') 
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
                installments_count,
                COUNT(DISTINCT transaction_id) AS transaction_count, 
                SUM(transaction_amount) as transaction_amount
            FROM transactions 
            WHERE transaction_date > (
                SELECT date(MAX(transaction_date), '-12 months') 
                FROM transactions
            )
            GROUP BY month, installments_count
            ORDER BY month, installments_count
            """
        
        @staticmethod
        def popular_categories():
            return """
            SELECT
                strftime('%Y-%m', transactions.transaction_date) AS month,
                merchants.category,
                COUNT(DISTINCT transactions.transaction_id) as transaction_count
            FROM merchants
            JOIN transactions ON merchants.merchant_id = transactions.merchant_id
            WHERE transaction_date > (
                SELECT date(MAX(transaction_date), '-12 months') 
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
                CAST(
                    CASE
                        WHEN payment_date IS NULL THEN julianday('now') - julianday(scheduled_date) 
                        WHEN payment_date > scheduled_date THEN julianday(payment_date) - julianday(scheduled_date)
                        ELSE 0
                    END AS INTEGER
                ) AS dpd
            FROM installments
            """
        
        @staticmethod
        def define_dpd90_rate():
            return """
            WITH DPD_Aggregate AS (
                SELECT 
                transaction_id,
                installment_number,
                CAST(
                    CASE
                        WHEN payment_date IS NULL THEN julianday('now') - julianday(scheduled_date) 
                        WHEN payment_date > scheduled_date THEN julianday(payment_date) - julianday(scheduled_date)
                        ELSE 0
                    END AS INTEGER
                ) AS dpd
            FROM installments)
            SELECT 
                transaction_id,
                CASE WHEN MAX(dpd) >= 90 THEN 1 ELSE 0 END as dpd90
            FROM DPD_Aggregate
            GROUP BY transaction_id
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
        def group_by_first_transaction():
            return """
            SELECT 
                MIN(strftime('%Y-%m', transaction_date)) AS month,
                user_id
            FROM transactions 
            WHERE transaction_date > (
                SELECT date(MAX(transaction_date), '-12 months') 
                FROM transactions
            )
            GROUP BY user_id
            ORDER BY month
            """

        @staticmethod
        def dpd90_status_after_months():
            return
        
        @staticmethod
        def dpd90_percentage_per_month():
            return
