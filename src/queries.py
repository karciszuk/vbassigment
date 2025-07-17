class SQL_Queries:
    
    class Portfolio:
        @staticmethod
        def new_customers():
            return """
            SELECT strftime('%Y-%m', registration_date) AS month, COUNT(DISTINCT user_id) AS user_count
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
            SELECT strftime('%Y-%m', Users.registration_date) AS month, COUNT(DISTINCT Users.user_id) AS user_count
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
            SELECT strftime('%Y-%m', transaction_date) AS month, COUNT(DISTINCT transaction_id) AS transaction_count, SUM(transaction_amount) as transaction_amount
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
            SELECT strftime('%Y-%m', transaction_date) AS month, 
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
            SELECT category, COUNT(DISTINCT Transactions.transaction_id) as transaction_count
            FROM merchants
            JOIN Transactions ON merchants.merchant_id = Transactions.merchant_id
            GROUP BY category
            ORDER BY transaction_count DESC
            """
    
    class Payment:
        @staticmethod
        def define_dpd_aggregate():
            return
        
        @staticmethod
        def define_dpd90_rate():
            return
        
        @staticmethod
        def calculate_dpd90_trend():
            return
    
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
