import sqlite3
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()


class SQL_Executor:
    def __init__(self):
        self.db_path = os.path.join(os.getenv("PYTHONPATH"), os.getenv("DB_PATH"))
        self.conn = self.create_connection()

    def create_connection(self) -> sqlite3.Connection:
        try:
            conn = sqlite3.connect(self.db_path)
            return conn
        except sqlite3.Error as e:
            print(f"Connection failed: {e}")
            raise

    def execute_query(self, query: str) -> None:
        try:
            df = pd.read_sql_query(query, self.conn)
            return df
        except sqlite3.Error as e:
            print(f"Query failed: {e}")
            raise

    def cleanup(self) -> None:
        if self.conn:
            self.conn.close()
        return True


if __name__ == "__main__":
    test = SQL_Executor()
    print(
        test.execute_query(
            """
        SELECT * 
        FROM transactions
        WHERE user_id = 1
        """
        )
    )

    print(
        test.execute_query(
            """
        SELECT * 
        FROM installments
        WHERE transaction_id = 4
        """
        )
    )
