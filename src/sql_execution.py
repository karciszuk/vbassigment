import sqlite3
import pandas as pd

class SQL_Executor():
    def __init__(self):
        self.db_path = 'D:/VB/viabill.db'
        self.conn, self.cur = self.create_connection()

    def create_connection(self):
        try:
            conn = sqlite3.connect(self.db_path)
            cur = conn.cursor()
            return conn, cur
        except sqlite3.Error as e:
            print(f"Connection failed: {e}")
            raise

    def execute_query(self, query):
        try:
            self.cur.execute(query)
            return self.cur.fetchall()
        except sqlite3.Error as e:
            print(f"Query failed: {e}")
            raise

    def display_results(self, results):
        results_df = pd.DataFrame(results, columns=[col[0] for col in self.cur.description])
        return results_df

    def cleanup(self):
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()
        return True