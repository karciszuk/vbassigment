import sqlite3
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()


class SQL_Executor:
    def __init__(self):
        self.db_path = os.getenv("DB_PATH")
        self.conn = self.create_connection()

    def create_connection(self):
        try:
            conn = sqlite3.connect(self.db_path)
            return conn
        except sqlite3.Error as e:
            print(f"Connection failed: {e}")
            raise

    def execute_query(self, query):
        try:
            df = pd.read_sql_query(query, self.conn)
            return df
        except sqlite3.Error as e:
            print(f"Query failed: {e}")
            raise

    def cleanup(self):
        if self.conn:
            self.conn.close()
        return True
