from sql_execution import SQL_Executor
from queries import SQL_Queries

db_path = 'D:/VB/viabill.db'
sql_e = SQL_Executor(db_path)

def main(query):
    try:
        results = sql_e.execute_query(query)
        for row in results:
            print(row)
    finally:
        sql_e.cleanup()

if __name__ == "__main__":
    main(SQL_Queries.monthly_users)