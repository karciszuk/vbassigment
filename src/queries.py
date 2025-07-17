class SQL_Queries:
    
    class Portfolio:
        @staticmethod
        def new_customers():
            return """
            SELECT
                strftime('%Y-%m', registration_date) AS month,
                COUNT(DISTINCT user_id) AS user_count
            FROM Users 
            WHERE registration_date > (
                SELECT date(MAX(registration_date), '-12 months') 
                FROM Users
            )
            GROUP BY month 
            ORDER BY month
            """
        
        @staticmethod
        def active_customers():
            return  """
            SELECT
                strftime('%Y-%m', Users.registration_date) AS month,
                COUNT(DISTINCT Users.user_id) AS user_count
            FROM Users
            JOIN Transactions ON Users.user_id = Transactions.user_id
             WHERE registration_date > (
                SELECT date(MAX(registration_date), '-12 months') 
                FROM Users
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
            FROM Transactions 
            WHERE transaction_date > (
                SELECT date(MAX(transaction_date), '-12 months') 
                FROM Transactions
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
            FROM Transactions 
            WHERE transaction_date > (
                SELECT date(MAX(transaction_date), '-12 months') 
                FROM Transactions
            )
            GROUP BY month, installments_count
            ORDER BY month, installments_count
            """
        
        @staticmethod
        def popular_categories():
            return """
            SELECT
                strftime('%Y-%m', Transactions.transaction_date) AS month,
                Merchants.category,
                COUNT(DISTINCT Transactions.transaction_id) as transaction_count
            FROM Merchants
            JOIN Transactions ON Merchants.merchant_id = Transactions.merchant_id
            WHERE transaction_date > (
                SELECT date(MAX(transaction_date), '-12 months') 
                FROM Transactions
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
            FROM Installments
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
            FROM Installments)
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
                Transactions.transaction_id,
                Transactions.user_id,
                Users.age,
                Users.income
            FROM Transactions
            JOIN Users ON Transactions.user_id = Users.user_id
            """
    
    class Vintage:
        @staticmethod
        def group_by_first_transaction():
            return

        @staticmethod
        def dpd90_status_after_months():
            return
        
        @staticmethod
        def dpd90_percentage_per_month():
            return
