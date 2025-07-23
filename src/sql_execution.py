import sqlite3
import pandas as pd
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


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

    def execute_query(self, query: str) -> pd.DataFrame:
        try:
            df = pd.read_sql_query(query, self.conn)
            self.validate_query_results(df)
            return df
        except sqlite3.Error as e:
            print(f"Query failed: {e}")
            raise

    def validate_query_results(self, df: pd.DataFrame) -> None:
        assert len(df) > 0, "Empty dataset"

    def __del__(self):
        if hasattr(self, "conn"):
            self.conn.close()
