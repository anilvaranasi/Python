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
#con.cursor().execute("PUT file://d:/data/data.csv:* @%ACCOUNTS")
#con.cursor().execute("PUT file://d:\data\data.csv @%ACCOUNTS")
con.cursor().execute("PUT file://d:\data\data2.csv @%ACCOUNTS")
#con.cursor().execute("PUT file://filepath:* @%ACCOUNTS")
#file://c:\data\data.csv
con.cursor().execute("COPY INTO ACCOUNTS")

# Putting Data
#con.cursor().execute("PUT file:///tmp/data/file* @%testtable")
#put file://c:\data\data.csv @~/staged;
#con.cursor().execute("PUT file:///loadersheet.csv* @%ACCOUNTS")