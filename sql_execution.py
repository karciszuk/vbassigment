import sqlite3

class SQL_Executor():
    def __init__(self, db_path):
        self.db_path = db_path
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

    def cleanup(self):
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()
        return True