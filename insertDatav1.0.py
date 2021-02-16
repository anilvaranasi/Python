#!/usr/bin/env python
import snowflake.connector
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
con.cursor().execute(
        "INSERT INTO ACCOUNTS(LAB, NAME) VALUES " + 
        "    ('labx24', 'accountx1'), " + 
        "    ('labx25', 'accountx2')")