class SQL_Queries:
    
    class Portfolio:
        @staticmethod
        def new_customers():
            return """
            SELECT COUNT(DISTINCT user_id) AS user_count, strftime('%Y-%m', registration_date) AS month 
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
            return 
        
        @staticmethod
        def transaction_volume():
            return
        
        @staticmethod
        def installment_plans():
            return
        
        @staticmethod
        def popular_categories():
            return
    
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
