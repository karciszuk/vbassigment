import sqlite3
import pandas as pd

class SQL_Executor():
    def __init__(self):
        self.db_path = 'D:/VB/viabill.db'
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
            return print(df.to_string(index=False))
        except sqlite3.Error as e:
            print(f"Query failed: {e}")
            raise

    def cleanup(self):
        if self.conn:
            self.conn.close()
        return True