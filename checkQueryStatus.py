#!/usr/bin/env python
import snowflake.connector
from snowflake.connector import ProgrammingError
import time
...
# Wait for the query to finish running and raise an error
# if a problem occurred with the execution of the query.
con = snowflake.connector.connect(
    user='VARANCONSULTING',
    password='Abcd123$',
    account='FN49743.us-east-2.aws',
    session_parameters={
        'QUERY_TAG': 'EndOfMonthFinancials',
    }
)
con.cursor().execute("ALTER SESSION SET QUERY_TAG = 'EndOfMonthFinancials'")
con.cursor().execute("USE WAREHOUSE COMPUTE_WH")
con.cursor().execute("USE DATABASE IDRREPORTS")
con.cursor().execute("USE SCHEMA PUBLIC")
try:
  query_id = cur.sfqid
  while con.is_still_running(conn.get_query_status_throw_if_error(query_id)):
    time.sleep(1)
except ProgrammingError as err:
  print('Programming Error: {0}'.format(err))