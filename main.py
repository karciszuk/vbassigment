from sql_execution import SQL_Executor
from queries import SQL_Queries
import pandas as pd

db_path = 'D:/VB/viabill.db'
sql_e = SQL_Executor(db_path)

def main(query):
    try:
        results = sql_e.execute_query(query)
        results_df = pd.DataFrame(results, columns=[col[0] for col in sql_e.cur.description])
        print(results_df)
    finally:
        sql_e.cleanup()

if __name__ == "__main__":
    query = SQL_Queries.Portfolio.new_customers()
    main(query)